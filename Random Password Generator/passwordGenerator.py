#! /usr/bin/python3

import random


def getWord(l):
    while True:
        try:
            word = random.choice(open(l).readlines()).split('\t')[-1]
            break
        except Exception:
            pass
    return word


if __name__ == '__main__':
    easy = open('easy.txt', 'r')
    hard = open('hard.txt', 'r')
    i = {}
    while True:
        i['wordType'] = input('''Select type of words you want in password:
        1> Hard
        2> Easy
        3> Select Randomly
    input: ''')
        if i['wordType'] in ['1', '2', '3']:
            break
        else:
            print('Enter correct input\n\n')
    while True:
        i['words'] = input('''\n\nEnter Number of words you want in your password:
    input: ''')
        try:
            i['words'] = int(i['words'])
            if i['words'] > 0:
                break
            else:
                raise ValueError(None)
        except Exception as e:
            print('Enter a positive integer')
    password = []
    for _ in range(i['words']):
        if i['wordType'] == '1':
            m = 1
        elif i['wordType'] == '2':
            m = 2
        else:
            m = random.randint(1, 2)
        if m == 1:
            password.append(getWord('hard.txt'))
        else:
            password.append(getWord('easy.txt'))
    print('Password: \n')
    for _ in password:
        print(_[:-1], end='')

    print('\n\nList of words in Password')
    for _ in password:
        print(_, end='')
