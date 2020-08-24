#!/usr/bin/env python3

def twitter(email):
    with open(combolist) as myFile:
        for num, line in enumerate(myFile, 1):
            if email[0] == line.split(':')[0][0] and email[1] == line.split(':')[0][1] and len(email) == len(line.split(':')[0]) and email[email.find('@')+1] == line.split(':')[0][line.find('@')+1]:
                print("[*] Found at line",num,':')
                password = line.split(':')
                print("Email:", password[0])
                print("Password:",password[1])
    myFile.close()

def instagram(email):
    with open(combolist) as myFile:
        for num, line in enumerate(myFile, 1):
            if email[0] == line.split(':')[0][0] and email[email.find('@')-1] == line.split(':')[0][line.find('@')-1] and len(email) == len(line.split(':')[0]) and email[email.find('@'):len(email)] == line.split(':')[0][line.find('@'):len(line.split(':')[0])]:
                print("[*] Found at line",num,':')
                password = line.split(':')
                print("Email:", password[0])
                print("Password:",password[1])

    myFile.close()

email = input("Enter the email you want to find please: ")
combolist = input("Enter the path of the combolist :")

print()

if '*' in email[email.find('@'):email.find('.')]:
    twitter(email)
else:
    instagram(email)
