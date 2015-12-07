#! /usr/bin/env pyton3

'''
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
Symbol Value:
    I 1 (unus)
    V 5 (quinque)
    X 10 (decem)
    L 50 (quinquaginta)
    C 100 (centum)
    D 500 (quingenti)
    M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The string in the form of a Roman numeral.
Precondition: 0 < number < 4000
'''

unus = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
decem = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX','LXX', 'LXXX', 'XC']
centum = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

#def checkio(n):
#    sn = str(n)    
#    bit = [int(c) for c in sn] 
#    bit = (4-len(sn)) * [0] + bit
#    print(bit)
#    f = (lambda j: j*'M', lambda j: centum[j], lambda j: decem[j], lambda j: unus[j])
#    print(([f[i](bit[i]) for i in range(4)]))
#    return bit[0]*'M'+centum[bit[1]]+decem[bit[2]]+unus[bit[3]]
#    

checkio = lambda n, f = (lambda j: j*'M', lambda j: centum[j], lambda j: decem[j], lambda j: unus[j]): ''.join([f[i]([(4-len(str(n))) * [0] + [int(c) for c in str(n)]][0][i]) for i in range(4)])

def test():
    for n in 1,2090,602,110,1110,1100,6,76,499,3888:
        print(checkio(n))

if __name__ == '__main__':
    test()
