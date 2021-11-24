'''
Author: Samuel James
Use: This program will run simple networking commands from a CLI GUI
Date: 11/16/21
Name: net.py
 
'''

import subprocess
import time
from pyfiglet import Figlet

menu = '''
+-------------------------------------------------+
+-------------------------------------------------+
+             QUICKNET TROUBLESHOOTING            +
+                                                 +
+-------------------------------------------------+
+-------------------------------------------------+
+       G - CLI Commands Glossary                 +
+       S - Speed Test Program
+       1 - netstat                               +
+       2 - ping by address                       +
+       3 - print route table                     +
+       4 - print arp table                       +
+       5 - get MAC Address                       +
+       6 - nslookup by domain                    +
+       7 - tracert specified address             +
+       8 - see all system info                   +
+       9 - check power config                    +
+       10 - check drivers                        +
+       11 - Show IPCONFIG                        +
+       12 - Show Power config settings           +
+       0 - EXIT PROGRAM                          +
+-------------------------------------------------+
+-------------------------------------------------+

'''

logo = '''
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''

def Glossary():
    print('''
          ***********************************
          * ~ ~ ~ ~ ~ ~ Glossary ~ ~ ~ ~ ~ ~*
          *_________________________________*
          * SYSTEMINFO - print all sys info *
          * IPCONFIG - Show IP configuration*
          * TASKLIST - Show all running     *
          *            tasks                *
          * TRACERT - Trace route to given  *
          *           Domain                *
          * REGEDIT - Open Windows Registry *
          * DRIVERQUERY - Show all drivers  *
          * NETSTAT - Network statistics    *
          * NSLOOKUP - Find public address  *
          * GETMAC - get mac address        *
          * FINDSTR - Windows CLI grep      *
          ***********************************
          
          ''')

def clr():
    subprocess.call("cls", shell=True)
    
def Menu():
    try:
        running = True
        while(running):
            print(menu)
            choice = input("Enter your choice: ")
            if(choice == '1'):
                print(p.renderText("Running network statistics..."))
                subprocess.call("netstat", shell=True)
            elif(choice == '2'):
                addr = input("Enter Address to Ping: \n")
                subprocess.call("ping "+ addr, shell=True)
            elif(choice == '3'):
                print(p.renderText("Printing route table..."))
                subprocess.call("route print", shell=True)
            elif(choice == '4'):
                print(p.renderText("Printing arp table..."))
                subprocess.call("arp -a", shell=True)
            elif(choice == '5'):
                print(p.renderText("Retrieving MAC address"))
                subprocess.call("getmac", shell=True)
            elif(choice == '6'):
                dom = input(p.renderText("Enter specific Domain: \n"))
                subprocess.call("nslookup " + dom, shell=True)
            elif(choice == '7'):
                rt = input("enter route to trace: \n")
                subprocess.call("tracert "+rt, shell=True)    
            elif(choice == '8'):
                print(p.renderText("Grabbing system information..."))
                subprocess.call("SYSTEMINFO", shell=True)
            elif(choice == '9'):
                print(p.renderText("Genberating battery report"))
                subprocess.call("POWERCFG /batteryreport", shell=True)
            elif(choice == '10'):
                print(p.renderText("running Driver Query..."))
                subprocess.call("driverquery", shell=True)
            elif(choice == '11'):
                print(p.renderText("pulling ipconfig..."))
                subprocess.call("ipconfig", shell=True)
            elif(choice == '12'):
                print(p.renderText("pulling battery settings..."))
                subprocess.call("powercfg /a", shell=True)
            elif(choice == 'G'):
                Glossary()
                time.sleep(5)
            elif(choice == 'S'):
                subprocess.call("Python Speed_test.py", shell=True)
                #time.sleep(5)
            elif(choice == '0'):
                print(gbye.renderText("See You Space Cowboy.."))
                exit(0)
        else:
            print("Invalid choice, please select a valid choice from 1-8")
    except KeyboardInterrupt:
        print("CLOSING PROGRAM, GOODBYE")

subprocess.call("COLOR 3", shell=True)
n = Figlet(font='larry3d')
p = Figlet(font='smslant')
b = Figlet(font='smkeyboard')
gbye = Figlet(font='banner3-D')
print (n.renderText('WELCOME'))
print(logo)
time.sleep(4)
subprocess.call("cls", shell=True)

print (n.renderText('QUICKNET PROGRAM'))
print (b.renderText('V1.3.3'))
time.sleep(4)
subprocess.call("cls", shell=True)

try:
    Menu()
except KeyboardInterrupt:
    Menu()
