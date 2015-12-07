#! /usr/bin/env python

'''
'''
#from string import uppercase 
#from string import lowercase 
#from string import digits
#
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits    = string.digits

#def checkio(data):
#
#    uppuer=lower=digit=False
#    if len(data) < 10:
#        return False
#    for c in data:
#        if c in lowercase:
#            lower = True
#        elif c in uppercase:
#            uppuer = True
#        elif c in digits:
#            digit = True
#    if uppuer and lower and digit:
#        return True
#    
#    return False
#
# Answer 1
checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    ) 
if __name__ == '__main__':
    print(checkio('bAse730onE4'))

# Answer 2
import re
 
DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')
 
def checkio(data):
    """
    Return True if password strong and False if not
     
    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False
     
    if not DIGIT_RE.search(data):
        return False
 
    if not UPPER_CASE_RE.search(data):
        return False
 
    if not LOWER_CASE_RE.search(data):
        return False
         
    return True

# Answer 3
f = lambda d, x:any(ord(t) & 96 == x for t in d)
checkio = lambda d: f(d, 32) & f(d, 64) & f(d, 96) & (len(d) > 9)
