#! /usr/bin/python3


def rot(n, cipher):
    for x in range(len(cipher)):
        if cipher[x] >= 65 and cipher[x] <= 91:
            if cipher[x] + n <= 91:
                cipher[x] += n
            else:
                cipher[x] += n - 26
        elif cipher[x] >= 91 and cipher[x] <= 122:
                if cipher[x] + n <= 122:
                    cipher[x] += n
                else:
                    cipher[x] += n - 26
    print("ROT", n, "= ", end="")
    for x in range(len(cipher)):
        print(chr(cipher[x]), end="")
    return print("\n")


if __name__ == '__main__':
    cipher = [ord(x) for x in input('Enter the String: \n')]
    for x in range(26):
        rot(x, cipher)
