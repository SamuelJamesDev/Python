import speedtest
speed = speedtest.Speedtest()
from pyfiglet import Figlet
import time

n = Figlet(font='banner3-D')
b = Figlet(font='cyberlarge')
l = Figlet(font='slant')

def Menu():
    while True:
        print('\a')
        menu = ('''
              +-----------------------------------------------------+
              +-----------------------------------------------------+
              +            1.) Download Speed Test                  +
              +            2.) Upload Speed Test                    +
              +            3.) Exit Program                         +
              +-----------------------------------------------------+
              +-----------------------------------------------------+
              ''')
        print(menu)
        choice=(input("Enter Your Choice: "))
        print('\a')
        if choice=='1':
            print(b.renderText('Counting...'))
            print((f"Download speed: {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s"))
        elif choice=='2':
            print(b.renderText('Counting...'))
            print(f"Upload speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
        elif choice=='3':
            print(n.renderText('See You Space Cowboy..'))
            quit()
        else:
            print("Please choose a valid option")

print(n.renderText('''SPEED  TEST'''))
Menu()
