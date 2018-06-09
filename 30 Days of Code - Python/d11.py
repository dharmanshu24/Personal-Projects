#!/bin/python3

if __name__ == '__main__':
    arr = []
    maxSum = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if i == 0 and j == 0:
                maxSum = sum
            elif sum > maxSum:
                maxSum = sum
    print(maxSum)
