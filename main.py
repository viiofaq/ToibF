import hashlib
import random
import string
import re
import pyhibp
from pyhibp import pwnedpasswords as pw
import requests
import itertools
from string import digits, punctuation, ascii_letters  # алфавит


def passgen():
    length = (input("Введите длину пароля: "))
    if length == "":
        length = 8
    chara = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chara) for _ in range(length))
    print(password)
    return password


def passhash():
    password = input("Введите пароль: ")
    passhashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(passhashed)
    return passhashed


def passcheck():
    password = input("Введите пароль: ")
    Bigcheck = (re.findall('[A-ZА-Я]', password))
    Speccheck = (re.findall('[.,:;!_*-+()/#¤%&)]', password))
    Numbercheck = (re.findall('[0123456789]', password))

    if len(Bigcheck) <= 0:
        print('Пароль не соответствует требованиям')
    elif len(Speccheck) <= 0:
        print('Пароль не соответствует требованиям')
    elif len(Numbercheck) <= 0:
        print('Пароль не соответствует требованиям')
    elif len(password) < 8:
        print("Пароль не соответствует требованиям")
    else: print("Действительный пароль")


def passlistchecker():
    with open('passlist.txt', 'r') as file:
        for line in file:
            Bigcheck = (re.findall('[A-ZА-Я]', line))
            Speccheck = (re.findall('[.,:;!_*-+()/#¤%&)]', line))
            Numbercheck = (re.findall('[0123456789]', line))

            if len(Bigcheck) <= 0:
                pass
            elif len(Speccheck) <= 0:
                pass
            elif len(Numbercheck) <= 0:
                pass
            elif len(line) < 8:
                pass
            else:
                print(line)


def leakcheck():
    with open('userlist.txt', 'r') as file:
        for line in file:
            a = line.split(',')
            name = a[0]
            password = a[1]
            pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
            resp = pw.is_password_breached(password=password)
            if resp:
                print("Пароль пользователя ",name," раскрыт")
            else:
                print("Пароль пользователя ", name, " не раскрыт")


def bruteforce():
    flag = 0
    possible_symbols = digits + ascii_letters + punctuation
    truepassword = input("Взламываемый пароль: ")
    password_length = input("Предполагаемая длина пароля: ")
    password_length = [int(item) for item in password_length.split("-")]

    for pass_length in range(password_length[0]+1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)

            if password == truepassword:
                print("Пароль подобран: ",password)
            else:
                pass
