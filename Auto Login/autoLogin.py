#! /usr/bin/python3
import logging
import datetime
import time
from grab import Grab
from getpass import getpass


def aCalc():
    return int(time.mktime(datetime.datetime.now().timetuple()) * 1000)


def logout(username):
    g = Grab()
    g.go('http://172.16.0.1:8090/logout.xml', post=[('username', username), ('a', aCalc), ('mode', '193'), ('producttype', '0')])


def login(username, password):
    print('Loggin in....')
    g = Grab()
    g.go('http://172.16.0.1:8090')
    g.doc.set_input('username', username)
    g.doc.set_input('password', password)
    g.doc.submit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    login(username, password)
    input('Press Enter to logout. Otherwise press Ctrl + C')
    logout(username)
