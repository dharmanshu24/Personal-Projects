#!/bin/python3

import sys

S = input().strip()
try:
    y = int(S)
    print(y)
except ValueError:
    print('Bad String')