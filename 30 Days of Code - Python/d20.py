#!/bin/python3

import sys

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False
    tries = 0
    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                tries += 1
    print('Array is sorted in {} swaps.'.format(tries))
    print('First Element: {}'.format(bad_list[0]))
    print('Last Element: {}'.format(bad_list[-1]))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

bubble(a)