# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:50:42 2021

@author: Samuel James
#bIKNOWTHATSRIGHT

I love my wife - this will send her random love messages when I run it.
"""
# this script requires an email that can have the 3rd party applications security turned off to send sms from gmail
import random
import smtplib
import pyfiglet

def SMS():
    
    # Working mobile fonts:
    # digital
    # bubble (Kinda?)
    # cybersmall
    # eftipiti
    # mini
    
    FUN = pyfiglet.figlet_format("I love you", font="digital")
    FUN2 = pyfiglet.figlet_format("ILY", font="cybersmall")
    
    BYE = pyfiglet.figlet_format("GOODBYE", font="slant")
    MSG = pyfiglet.figlet_format("Message Sent:", font="slant")
    
    num = random.randint(0, 9)
    
    body = ['I love you honey, I hope you are having a good day!!!!!!!!!!!!!!!!!!!!', 
        'Every day I look at you and I feel the same way as when you first yelled at me to help you move that couch, I love you', 
        'yoyoyoyo I love you dood', 
        'Your spirit animal is a giraffe in sunglasses lol, I love you', 
        'I love you, If we both get reincarnated as dogs I promise not to make fun of you for being a small dog', 
        'I love you, heres a long neck donkey fact: Giraffes can run as fast as 35 miles an hour over short distances, or cruise at 10 mph over longer distances.', 
        'I love you, you Gorgeouus bad bitch', 
        'I love you savannahBannana',
        FUN,
        FUN2
        ]
    
    to_num = "############@messaging.sprintpcs.com" 
    # is the # that you are messages i.e. 123 123 1234 
    auth = ('<EMAIL>', '<PASSWORD>', 'Samuel')
    Subject = (' ')
    
    sent = body[num]
    
    message = ( "From: %s\r\n" % auth[2]
        + "To: %s\r\n" % to_num
        + "Subject: %s\r\n" % Subject
        + "\r\n"
        + sent
        )

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    ver = smtplib.SMTP( "smtp.gmail.com", 587 )
    ver.starttls()
    ver.login(auth[0], auth[1])
    
    ver.sendmail( auth[0], to_num, message)
    print(MSG)
    
    print(sent)
    
    print(BYE)
    
SMS()
