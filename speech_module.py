#! /usr/bin/env pyton3

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

X='thir four fif six seven eigh nine'.split()
A=' one two three four five six seven eight nine ten eleven twelve'.split(' ')+[s+'teen'for s in X]
B=['twenty']+[s.replace('u','')+'ty'for s in X]
f = lambda n, v = 0:v and [A[v],'hundred'] + f(n % 100) or n<20 and [A[n]] or [B[n//10-2]]+f(n%10)
checkio = lambda n:' '.join(f(n, n//100)).strip()


def f(n, v=0):
    if v:
        return [A[v], 'hundred'] + f(n % 100)
    elif n < 20:
        return [A[n]]
    else:
        return [B[n // 10 - 2]] + f(n % 10)
def checkio(n):
    return ' '.join(f(n, n//100)).strip()

def checkio(n, d=dict(enumerate(" one two three four five six seven eight nine ten eleven twelve".split(" ")))):
    def i(s, j=iter("o en ree ir ve f t ".split(" "))):
        for k in j: s = __import__("re").sub(k + "$", next(j), s)
        return s
    return (d[n//100]+" hundred "*(n>99)+d.get(n%100,n%100<20and i(d[n%10])+"teen"or i(d[n//10%10]).replace("u","")+"ty "+d[n%10])).strip()

print(checkio(333))
