#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    x = bin(n)
    lstreak = 0
    streak = 0
    for ch in x:
        if ch == '1':
            streak += 1
        else:
            streak = 0
        if streak > lstreak:
            lstreak = streak
    print(lstreak)
