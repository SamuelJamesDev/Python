# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:20:42 2022

@author: SamuelJames
"""

import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.asciiart.eu/"

bufftop = '+'*50
buffbott = '_'*50

def asciiOptions():
    options = []
    r = requests.get(url, verify=False)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    test = soup.find('div', class_="directory-columns")
    dirc = (test.findAll('a'))
    count = 0
    for d in dirc:
        print(count, " - ", d.text)
        options.append(d.text.lower().replace(" ", "-"))
        count += 1

    print('Please select one of the following options:\n')
    inp = int(input('Enter your choice:\n'))
    try:
        if inp > count or inp < 0:
            print("INVALID ENTRY, TRY AGAIN...")
            asciiOptions()
        else:
            subMenuOptions(url + options[inp])
    except ValueError:
        print("Invalid Entry, try again...")
        asciiOptions()
    
def subMenuOptions(urlIn):
    options2 = []
    r = requests.get(urlIn, verify=False)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    test = soup.find('div', class_="directory-columns")
    dirc = (test.findAll('a'))
    
    count2 = 0
    print('Please select one of the following options:\n')
    for d in dirc:
        print(count2, " - ", d.text)
        options2.append(d.text.lower())
        count2 += 1
    try:
        inp2 = int(input('Enter your choice:\n'))
        if inp2 > count2 or inp2 < 0:
            print("INVALID ENTRY, TRY AGAIN...")
            subMenuOptions(urlIn)
        else:
            displayArt(urlIn + '/' + options2[inp2])
    except ValueError:
        print("Invalid Entry, try again...")
        subMenuOptions(urlIn)

def displayArt(urlIn2):
    options2 = []
    print(urlIn2)
    r = requests.get(urlIn2, verify=False)

    soup = BeautifulSoup(r.content, 'html.parser')
    pre = (soup.findAll('pre'))
    for t in pre:
        print(bufftop)
        print(t.text, '\n\n', buffbott)
        time.sleep(1)
    
    
if __name__ == "__main__":
    try:
        asciiOptions()
    except KeyboardInterrupt:
       print("GOODBYE!")
