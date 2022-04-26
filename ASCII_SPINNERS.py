# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:24:43 2022

@author: SamuelJames
"""
import time
from colorama import init
from termcolor import colored
import os
# use Colorama to make Termcolor work on Windows too
init()

arrow = '← ↖ ↑ ↗ → ↘ ↓ ↙'
eye = ['◐', '◓', '◑', '◒']
bar = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃','▁']
boxEye = ["◰", "◳", "◲","◱"]
blink = ['(o)(o)', '(-)(-)']
bar_horz = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
vert = ["▏","▎","▍","▌","▋","▊","▉","▊","▋","▌","▍","▎"]
star = ["✶","✸","✹","✺","✹","✷"]
noise = ["▓","▒","░"]
bounce =  ["▖","▘","▝","▗"]
balOfDeath = ["◜","◠","◝","◞","◡","◟"]
toggle = ["■","□","▪","▫"]
toggle2 = ["⦾","⦿"]
toggle3 = ["㊂","㊀","㊁"]
toggle4 = ["⊶","⊷"]
monkey = ["🙈 ","🙈 ","🙉 ","🙊 "]
clock = ["🕛 ","🕐 ","🕑 ","🕒 ","🕓 ","🕔 ","🕕 ","🕖 ","🕗 ","🕘 ","🕙 ","🕚 "]
fun = ["🤜\u3000\u3000\u3000\u3000🤛 ","🤜\u3000\u3000\u3000\u3000🤛 ","🤜\u3000\u3000\u3000\u3000🤛 ","\u3000🤜\u3000\u3000🤛\u3000 ","\u3000\u3000🤜🤛\u3000\u3000 ","\u3000🤜✨🤛\u3000\u3000 ","🤜\u3000✨\u3000🤛\u3000 "]
sound = ["🔈 ","🔉 ","🔊 ","🔉 "]
heart = ["💛 ","💙 ","💜 ","💚 ","❤️ "]
earth = ["🌍 ","🌎 ","🌏 "]
moon = ["🌑 ","🌒 ","🌓 ","🌔 ","🌕 ","🌖 ","🌗 ","🌘 "]
run = ["🚶 ","🏃 "]
dot = ["⠁","⠁","⠉","⠙","⠚","⠒","⠂","⠂","⠒","⠲","⠴","⠤","⠄","⠄","⠤","⠠","⠠","⠤","⠦","⠖","⠒","⠐","⠐","⠒","⠓","⠋","⠉","⠈","⠈"]
pipe = ["┤","┘","┴","└","├","┌","┬","┐"]
mind = ["😐 ","😐 ","😮 ","😮 ","😦 ","😦 ","😧 ","😧 ","🤯 ","💥 ", "✨ ","\u3000 ","\u3000 ","\u3000 "]
soccer = [" 🧑⚽️       🧑 ","🧑  ⚽️      🧑 ","🧑   ⚽️     🧑 ","🧑    ⚽️    🧑 ","🧑     ⚽️   🧑 ","🧑      ⚽️  🧑 ","🧑       ⚽️🧑  ","🧑      ⚽️  🧑 ","🧑     ⚽️   🧑 ","🧑    ⚽️    🧑 ","🧑   ⚽️     🧑 ","🧑  ⚽️      🧑 "]
diamond = ["🔸 ","🔶 ","🟠 ","🟠 ","🔶 ","🔹 ","🔷 ","🔵 ","🔵 ","🔷 "]
hands = ["🤘 ","🤟 ","🖖 ","✋ ","🤚 ","👆 "]
weather = ["☀️ ","☀️ ","☀️ ","🌤 ","⛅️ ","🌥 ","☁️ ","🌧 ","🌨 ","🌧 ","🌨 ","🌧 ","🌨 ","⛈ ","🌨 ","🌧 ","🌨 ","☁️ ","🌥 ","⛅️ ","🌤 ","☀️ ","☀️ "]
kisses = ["😗", "😙", "😚", "😘"]
covid = ["😷", "🤒", "🤧", "🤢", "🤮"]
age = ["👶", "👦", "🧔", "👨‍🦳"]
decompose = ["😧", "😱", "💀", "👻"]
finspin = ["👈", "🖕", "👉", "👇"]
flags = ["🏳️‍🌈", "🏳️‍", "🏴‍", "🚩"]
square = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "⬛"]
weapon = ["🗡", "🛠", "⚔"]
sleepy = ["😔", "🤤", "😪", "😴"]
hacker = ["🧑‍💻", "👨‍💻"]
bat = ["[🦇\u3000\u3000\u3000]", "[\u3000🦇\u3000\u3000]", "[\u3000\u3000🦇\u3000]", "[\u3000\u3000\u3000🦇]", "[\u3000\u3000🦇\u3000]", "[\u3000🦇\u3000\u3000]"]
whale = ["🐳", "🐋", "🐬"]


allnames = '''
All package loadbar names:\n
arrow:↑ , eye:◐ , earth🌍 , moon🌑 , heart💛, \n
bar:▇ , boxEye:◰, blink:(o)(o) , bar_horz:[■□□□□□□□□□] , vert:▌, \n
star:✸ , noise:▒ , bounce:▖, balOfDeath:◠ , toggle:□, \n
toggle2:⦾ , toggle3:㊂ , toggle4: ⊷ , monkey:🙉 , clock:🕛, sound:🔉 , \n
fun:🤜\u3000🤛 , run:🏃 , dot:⠙ , pipe: ┤ , mind: 😐, \n
soccer:🧑⚽️ 🧑 , diamond: 🔸 , weather:🌤 , kisses: ☺, \n
covid: 🤮, age: 👶 , decompose:👻 , finspin: 👇 , flags: 🚩 \n
square: 🟪 , weapon: 🗡 , sleepy:😴 , hacker:👨‍💻 , bat: , 🦇 \n
whale: 🐳
'''
     
def getLoadNames():
    print(allnames)

def LoadingDemo():
    running = [whale, bat, hacker, sleepy, weapon, square, flags, finspin, decompose, age, covid, kisses, arrow,eye, earth,moon,heart,bar,boxEye,blink,bar_horz,vert,star,noise,bounce,balOfDeath,toggle,toggle2,toggle3,toggle4,monkey,clock,sound,fun,run,dot,pipe,mind,soccer,diamond,weather]
    for i in range(len(running)):
        for t in range(3):
            for j in range(len(running[i])):
                print(colored((running[i][j]*5), 'green', 'on_grey'), end = '\r')
                time.sleep(.25)
        os.system('cls')
        
#loading animation test
def loading(arr):
    for y in range(10):
        for i in range(len(arr)):
            print(colored((arr[i]*5), 'green', 'on_grey'), end = '\r')
            time.sleep(.25)
