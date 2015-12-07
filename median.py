#! /usr/bin/env python

def median(L):
    '''return the median of the list'''
    L.sort()
    leng = len(L)
    if leng % 2 == 1:
        return L[leng//2]
    else:
        return (L[leng//2-1] + L[leng//2])/2.
        
if __name__ == 'checkio.median':
    #print checkio(list(range(1000000))) 
    print(median([1,2,3,4,5]))
