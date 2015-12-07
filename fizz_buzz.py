#! /usr/bin/env python3

def checkio(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'Fizz Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


if __name__ == '__main__':
    for n in 15,6,5,7:
        print(checkio(n))
