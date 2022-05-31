"""

@author: SamuelJames
@Name: R3APSCAN

to open python webserver - 
python3 -m http.server 8080
"""

import pyfiglet
import sys
import socket
from datetime import datetime
import subprocess
import time
from alive_progress import alive_bar
import ssl
from scapy.all import ARP, Ether, srp
import requests
import os
from colorama import init
from termcolor import colored
import os
os.environ['CURL_CA_BUNDLE'] = ""
# use Colorama to make Termcolor work on Windows too
init()

ld = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃','▁']
prt = []
vul_ports = [7, 22, 80, 443, 1434, 3389, 8000, 8080, 9080]
ascii_banner = pyfiglet.figlet_format("R3AP3R SCANNER")
exit_banner = pyfiglet.figlet_format("GOODBY3 R3AP3R...")
print(ascii_banner)

def loading():
    for j in range(1):
        for i in range(len(ld)):
            print(colored(ld[i]*60, 'green', 'on_grey'), end = '\r')
            time.sleep(.5)
            
def get_mac_details(mac_address):
      
    # We will use an API to get the vendor details
    url = "https://api.macvendors.com/"
      
    # Use get method to fetch details
    response = requests.get(url+mac_address)
    if response.status_code != 200:
        raise Exception("[!] Invalid MAC Address!")
        menu()
    else: 
        print('DEVICE:\n', response.content.decode())
        menu()

def sndout(target, port):
    message = """GET /  HTTP/1.1
        Host: 127.0.0.1
        Connection: keep-alive
        """

    host = (target, port)
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose=purpose)

    with socket.create_connection(host) as sock:
        with context.wrap_socket(sock, server_hostname=host[0]) as wrapped:

            wrapped.send(message.encode())
            modifiedMessage = wrapped.recv(2048).decode("ISO-8859-1")
            print(modifiedMessage)

def neighbor():
    print('SCANNING FROM HOST:\n')
    host = socket.gethostbyname(socket.gethostname())
    print(host)
    target_ip = host[0:9] + "1/25"
    print("Targeting range: " + target_ip)
    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})


    # print clients
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

        if (client['mac'] == "f4:f5:e8:37:67:92"):  #Testing mac address filter
            print("Success")
    
    target_ip2 = "SOMEGENERIC /24 IP"
    print('\nSCANNING FROM GENERIC IP:\n' + target_ip2)
    
    
    # IP Address for the destination
    # create ARP packet
    arp2 = ARP(pdst=target_ip2)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether2 = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet2 = ether2/arp2

    result2 = srp(packet2, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients2 = []

    for sent, received in result2:
        # for each response, append ip and mac address to `clients` list
        clients2.append({'ip': received.psrc, 'mac': received.hwsrc})


    # print clients
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients2:
        print("{:16}    {}".format(client['ip'], client['mac']))

        if (client['mac'] == "YOUR TEST MAC ADDRESS"):  #Testing mac address filter
            print("Success")
    
def getData(target, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target, port))
    for i in range(10):
        time.sleep(5)
        data = client_socket.recv(512)
        if data.lower() == 'q':
            client_socket.close()
            break

        print("RECEIVED: %s" % data)
        data = input("SEND( TYPE q or Q to Quit):")
        client_socket.send(data)
        if data.lower() == 'q':
            client_socket.close()
            break

def break_port(target, port):
    print('Open ports: ')
    for port in range(len(prt)):
        print(port, ': ', prt[port])
    cp = input('Enter The port to nmap:\n')
    print('running subprocess on port: ', cp + '\nCommand: nmap -A -p'+str(cp)+' '+str(target))
    
    
    
    p = subprocess.Popen('nmap -A -p'+str(cp)+' '+str(target), shell=True)
    p.communicate()
    sndout(target, port)
    #print('RETRIEVING PORT DATA')
    #getData(target, port)

def getTarget():
    name = input('Enter taret IP:\n')
     
    # translate hostname to IPv4
    target = socket.gethostbyname(name)
    print('Target Aquired ' + target)
    return target

def quickscan(target):
    prt.clear()
    time1 = datetime.now()
    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(time1))
    print("-" * 50)
    try:
     
        # will scan ports between 1 to 65,535
        with alive_bar(9) as bar:
            for port in vul_ports:
                time.sleep(.005)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
         
                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is VULNERABLE".format(port))
                    prt.append(port)
                else:
                    print('Port {} is LOCKED'.format(port))
                bar()
                s.close()
                
        inp = input('Would you like to breach a port? [Y/N]\n')
        if inp == 'y' or inp == 'Y':
            break_port(target, prt)
        else:
            print('Returning to main menu...')
            menu()
    except socket.gaierror:
        print("\n\tHostname Could Not Be Resolved !!!!")
        menu()
    except socket.error:
        print("\n\tServer not responding !!!!")
        menu()
        
def fullscan(target):
    try:
     
        # will scan ports between 1 to 65,535
        with alive_bar(65535) as bar:
            for port in range(1,65535):
                time.sleep(.005)
                bar()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
         
                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is open".format(port))
                else:
                    print('Port {} is LOCKED'.format(port))
                s.close()
         
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

ports = '''
Port Number\tProtocol[s]\tPort Service
7\t\tTCP, UDP\tEcho
19\t\tTCP, UDP\tChargen
20\t\tTCP, FTP\t\t[File Transfer Protocol]
21\t\tTCP\t\tFTP Control
22\t\tTCP\t\tSSH
23\t\tTCP\t\tTelnet
25\t\tTCP\t\tSMTP [Simple Mail Transfer Protocol]
37\t\tTCP, UDP\tTime
53\t\tUDP\t\tDNS [Domain Name System]
69\t\tUDP\t\tTFTP [Trivial File Transfer Protocol]
79\t\tTCP, UDP\tFinger
80\t\tUDP\t\tHTTP [Hyptertext Transfer Protocol]
110\t\tTCP\t\tPOP3 [Post Office Protocol v.3]
111\t\tTCP,UDP\tSUN.RPC [Remote Procedure Calls]
135	\tTCP,UDP\tRDC/DCE [Endpoint Mapper] – Microsoft networks
137-9,445\tTCP,UDP\t\tNetBIOS over TCP/IP
161\t\tTCP,UDP\t\tSNMP [Simple Network Management Protocol]
443\t\tTCP\t\tHTTPS [HTTP over TLS]
512-514\t\tTCP\t\tBarkley r-services and r-commands [e.g., rlogin, rsh, rexec]
1433\t\tTCP,UDP\tMicrosoft SQL Server [ms-sql-s]
1434\t\tTCP,UDP\tMicrosoft SQL Monitor [ms-sql-m]
1723\t\tTCP\t\tMicrosoft PPTP VPN
3389\t\tTCP\t\tWindows Terminal Server
8080\t\tTCP\t\tHTTP proxy
'''
def menu():
    
    men = " __________________________________\n|             0-EXIT               |\n|             1-QSCAN              |\n|             2-FULLSCAN           |\n|             3-PORTS              |\n|             4-NEIGHBOR SCAN      |\n|             5-NSLOOKUP           |\n|__________________________________|"
    print(men)
    try:
        choice = input('Choose your option: ')
        if choice == '0':
            print(exit_banner)
            exit()
        elif choice == '1':
            target = getTarget()
            quickscan(target)
            menu()
        elif choice == '2':
            target = getTarget()
            fullscan(target)
            menu()
        elif choice == '3':
            loading()
            print(ports)
            menu()
        elif choice == '4':
            neighbor()
            inp = input('Would you like to find vendor from MAC Address? [Y/N]\n')
            if inp == 'y' or inp == 'Y':
                addr = input('Enter the MAC address to scan: \n')
                get_mac_details(str(addr))
            else:
                print('Returning to main menu...')
                menu()
            menu()
        elif choice == '5':
            t = input("Enter target for NSLOOKUP:\n")
            subprocess.Popen('nslookup ' + t, shell=True)
            time.sleep(5)
            menu()
        else:
            print('INVALID ENTRY.. Please try again..')
            menu()
    except KeyboardInterrupt:
        print("\n\tExiting Program !!!!")
        sys.exit()
menu()
