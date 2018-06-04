#!/bin/python3

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        e = ['']
        o = ['']
        for i in range(len(s)):
            if i % 2 == 0:
                o.append(s[i])
            else:
                e.append(s[i])

        e = ''.join(e)
        o = ''.join(o)
        print('{} {}'.format(o, e))
