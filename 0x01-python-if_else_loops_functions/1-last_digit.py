#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l_digit = abs(number) % 10 
print('Last digit of', number, 'is', l_digit, 'and', end=' ')

if l_digit > 5:
    print('is greater then 5')
elif l_digit == 0:
    print('is 0')
else:
    print('is less than 6 and not 0')
