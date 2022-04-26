"""
Created on Mon Mar 28 07:46:49 2022

@author: SamuelJames
"""

import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import webbrowser

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://stackoverflow.com/"

bufftop = '+'*50
buffbott = '_'*50
#this will legit grab all href from an html page
def hrefTest():
    links = []
    titles = []
    term = input("\nGive me a topic: ")
    r = requests.get("https://stackoverflow.com/questions/tagged/" + str(term), verify=False)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    for div in soup.findAll('h3', attrs={'class':'s-post-summary--content-title'}):
        titles.append(div.find('a').contents[0])     
        links.append(url + div.find('a')['href'])
    chooseLink(links, titles)

def chooseLink(links, titles):
    for i in range(len(links)):
        print(bufftop)
        print("Article Number - ", i)
        print("TITLE - ", titles[i])
        print("link - ", links[i])
        print(buffbott)
    while True:
        inp2 = input("Enter the number corresponding to the article you would like to view: \n")
        if inp2 == 'EXIT' or inp2 == 'Exit' or inp2 == 'exit':
            inp3 = input('Choose another search? [Y \ N] \n')
            if inp3 == 'Y' or inp3 == 'y':
                hrefTest()
            else:
                print("Goodbye!")
                exit()
        else:
            webbrowser.open(links[int(inp2)], new=0, autoraise=True)

if __name__ == '__main__':
    try:
        hrefTest()
    except KeyboardInterrupt:
        print("Goodbye!")
