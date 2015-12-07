#! /usr/bin/env python

def checkio(L):
    ul = list(set(L))
    co = {}
    print ul
    for i in ul:
        co[i] = L.count(i)

    return [y for y in L if y in [x for x in ul if co[x] > 1]]
    return [x for x in L if L.count(x) > 1]
if __name__ == '__main__':
    print checkio([5,5,5,5,5])

