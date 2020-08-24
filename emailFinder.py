#!/usr/bin/env python3

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

email = input("Enter the email you want to find please: ")
combolist = input("Enter the path of the combolist :")

print()

if '*' in email[email.find('@')+1:email.find('.')]:
    if not twitter(email):
        print("[*] Email not found.")
else:
    if not instagram(email):
        print("[*] Email not found.")
