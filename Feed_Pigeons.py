#! /usr/bin/env pyton3

from functools import reduce

# Solution 1
def checkio(n):
    p = [0]
    N, new, t = 0, 0, 0
    while n > 0:
        t = t + 1
        new += 1
        #N = reduce((lambda x, y: x + y), range(1, t+1))
        N = t*(t+1)/2
        p = p + [0]*new
        for i in range(N):
            if n > 0:
                p[i] += 1
                n = n - 1
            else:
                break

    return len([x for x in p if x >0])

def test():
    for i in range(1,11):
        print(checkio(i))
# Solution 2
checkio = lambda n, y=0, i=0: n<y and max(n, y-i+1) or checkio(n-y, sum(range(i+1)), i+1)
# y: Total Pigeons at nth minites
# i: New Pigeons at nth minites
# n: feed remains at nth minites

if __name__ == '__main__':
    test()
