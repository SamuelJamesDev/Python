"""
Created on Tue Apr 26 14:06:59 2022

@author: SamuelJames
"""
import requests 
import wikipedia
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
import os
os.environ['CURL_CA_BUNDLE'] = ""
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bufftop = '+'*50
buffbott = '_'*50

# print the summary of what python is
def grabWiki():
    inp = str(input("Enter your search term:\n"))
    result = list(wikipedia.search(inp))
    print('All Results:\n',result)
    
    for i in (result):
        print(bufftop)
        print(i)
        try:
            check = wikipedia.summary(str(i))
            print(check)
            print(buffbott)
        except wikipedia.exceptions.PageError:
            print('PAGE NOT FOUND')
            print(buffbott)
        except wikipedia.exceptions.DisambiguationError:
            print('NO DISAMBIGUATION FOUND')
            
grabWiki()
