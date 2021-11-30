# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:14:34 2021

@author: SamuelJames
#USE: Print all email subjects, senders and what # email in inbox contains a given string. 
"""

"""Script to fetch email from outlook."""

import win32com.client
from datetime import datetime, timedelta

def extract(regexStr):
    """Get emails from outlook."""
    items = []
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # "6" refers to the inbox
    messages = inbox.Items
    i = 0
    for msg in list(messages):
        i += 1
        if(regexStr in msg.Body):
            print('_______________________________________________')
            print('EMAIL #: ', i)
            print('Sender: ',msg.Sender)
            print('Subject: ',msg.Subject)
            #print(msg.Body)

inp = input("Enter String to Search In Emails...\n")
extract(inp)
