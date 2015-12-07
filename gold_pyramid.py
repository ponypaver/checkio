#! /usr/bin/env python3

def count_gold(pyramid):
    s = pyramid[0][0]
    pos = 0
    for nl, l in enumerate(pyramid[1:]):
        pos = pos if l[pos] > l[pos+1] else pos+1
        s += l[pos]

    return s

def test():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    ))) #== 23, "First example"
    print(count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )))# == 15, "Second example"
    print(count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )))# == 18, "Third example" 

if __name__ == '__main__':
    test()

