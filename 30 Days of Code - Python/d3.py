#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    if N % 2 is 0:
        if N > 20 or (N > 1 and N < 6):
            print('Not ', end='')
    print('Weird')
