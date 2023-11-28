#!/usr/bin/python3
for i in range(0, 100)
        print('0{:d}'.format(i), end=', 'if i <= 9)
        print('{:d}'.format(i), end=', ' if i == 99 else ' ')
