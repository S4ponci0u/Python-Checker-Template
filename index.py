import json
from os import system
import easygui
import ctypes
from truecolor import fg, reset
import time
from GradientGen import PrintGradient, PrintLinearGradient

# Program variables
checker_title = "S4p Checker"
author = "S4ponci0u"

# Accounts stats
total_bad = 0
total_checked = 0
total_hits = 0

def main():
    # feel free to customize the title, if you dont know how to make ascii art, just go to 
    # http://www.patorjk.com/software/taag/
    title = '''
  ▄████████    ▄████████    ▄███████▄ 
  ███    ███   ███    ███   ███    ███ 
  ███    █▀    ███    ███   ███    ███ 
  ███          ███    ███   ███    ███    
▀███████████ ▀███████████ ▀█████████▀        
         ███   ███    ███   ███
   ▄█    ███   ███    ███   ███ 
 ▄████████▀    ███    █▀   ▄████▀                                                          
    '''
    system('cls')
    # change title of the windows
    ctypes.windll.kernel32.SetConsoleTitleW(f"{checker_title} | By: {author} | Checked: 0 | Hits: 0 | Bad: 0")
    PrintLinearGradient("#C33764", "#1D2671", title)
    print(f"{fg('#1C08FF')}\t[+] {fg('#87B5F5')}By: {author}{reset}")
    print(f"{fg('#1C08FF')}\t[+] {fg('#87B5F5')}Select the combo{reset}")
    try:
        combo = easygui.fileopenbox()
    except:
        print('\t[!] No combo selected')
        exit()

    # you can also use proxys, just copy paste the code below and change the variable name
    print(f"{fg('#1C08FF')}\t[+] {fg('#87B5F5')}Checking started!{reset}")
    with open(combo, 'r') as f:
        for line in f:
            email, password = line.split(':')
            check(email, password)

def update_title(checked: bool = None, hit: bool = None, bad:bool = None):
    if (checked):
        global total_checked
        total_checked += 1
    if (hit):
        global total_hits
        total_hits += 1
    if (bad):
        global total_bad
        total_bad += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"{checker_title} | By: {author} | Checked: {total_checked} | Hits: {total_hits} | Bad: {total_bad}")


def check(email:str, password:str):
    # define your code here!
    hit = True

    if (hit):
        print(f"{fg('green')}\t[+] {fg('white')}Hit: {email}:{password}{reset}")
        update_title(checked=True, hit=True)
    elif (hit == False):
        update_title(checked=True, bad=True)
main()
