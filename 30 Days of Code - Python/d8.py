#! bin/python3

if __name__ == '__main__':
    phoneBook = {}
    for _ in range(int(input())):
        name, number = input().split(' ')
        phoneBook[name] = int(number)
    while True:
        key = input()
        if key in phoneBook:
            print('{}={}'.format(key, phoneBook[key]))
        else:
            print('Not found')
