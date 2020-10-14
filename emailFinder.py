#!/usr/bin/env python3

import re
import sys
import os

def twitter(email):
    c=0
    with open(combolist) as myFile:
        for num, line in enumerate(myFile, 1):
            if email[0] == line.split(':')[0][0] and email[1] == line.split(':')[0][1] and len(email[0:email.find('@')]) == len(line.split(':')[0][0:line.find('@')]) and email[email.find('@')+1] == line.split(':')[0][line.find('@')+1]:
                print("[*] Found at line",num,':')
                password = line.split(':')
                print("Email:", password[0])
                print("Password:",password[1])
                c+=1
    myFile.close()
    return False if c == 0 else True
        

def instagram(email):
    c=0
    with open(combolist) as myFile:
        for num, line in enumerate(myFile, 1):
            if email[0] == line.split(':')[0][0] and email[email.find('@')-1] == line.split(':')[0][line.find('@')-1] and len(email[0:email.find('@')]) == len(line.split(':')[0][0:line.find('@')]) and email[email.find('@'):len(email)] == line.split(':')[0][line.find('@'):len(line.split(':')[0])]:                
                print("[*] Found at line",num,':')
                password = line.split(':')
                print("Email:", password[0])
                print("Password:",password[1])
                c+=1
    myFile.close()
    return False if c == 0 else True

def emailChecker(mail):
    if not (re.fullmatch(r"[^@]+@[^@]+\.[^@]+", mail)):
        print("Enter a valid email please.")
        return False
    return True

def combolistChecker():
    c = 0
    currentDirectory = os.getcwd()
    files = os.listdir(currentDirectory)
    for file in files:
        if file.endswith('.txt'):
            c += 1
            wordlist = file
    if c == 1:
        answer  = input("[*] Combolist detected, do you want to use "+wordlist+"? (Y/n) ")
        if answer == '' or answer.lower() == 'y':
            return wordlist
        else:
            combolist = input("Enter the path of the combolist : ")
    elif c > 1:
        print("[!] Multiple combolists detected.\n")
        for file in files:
            if file.endswith('.txt'):
                answer = input("Do you want to use " + file+"? (Y/n) ")
                if answer == '' or answer.lower() == 'y':
                    return file
        print("[!] No more combolists detected.")
        combolist = input("Enter the path of the combolist : ")
    else:
        combolist = input("Enter the path of the combolist : ")
    return combolist

try:
    email = input("Enter the email you want to find please: ")
    while not emailChecker(email):
        email = input("Enter the email you want to find please: ")
    combolist = combolistChecker()

    print()

    if '*' in email[email.find('@')+1:email.find('.')]:
        if not twitter(email):
            print("[*] Email not found.")
    else:
        if not instagram(email):
            print("[*] Email not found.")
except FileNotFoundError:
    print("[!] Combolist not found")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n[*] User quit")
    sys.exit(1)
