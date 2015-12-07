#! /usb/bin/env

import math
def is_prime(n):
    if n % 2 == 0 and n > 2 or n < 2: 
        return False
    if all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)) and str(n) == str(n)[::-1]:
        return True;

def golf(n):
    while True:
        if is_prime(n+1):
            return (n+1)
        else:
            print(n)
            n = n+1

print(golf(0))
