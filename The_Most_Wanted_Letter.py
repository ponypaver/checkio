#! /usr/bin/env python3

'''
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis. A string (unicode for py2.7).

Output: The most frequent letter in lower case. A string.

Example:

checkio("hello world!") == "l"
checkio("how do you do?") == "o"
checkio("one") == "e"
checkio("oops!") == "o"
checkio("aaaooo!!!!") == "a"
checkio("abe") == "a"

'''
#from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
import string

def checkio(text):
    #dletters = {}
    #letters = [x.lower() for x in text if x in lowercase or x in uppercase]
    ##print(letters)
    #for x in letters:
    #    lc = letters.count(x)
    #    if lc in dletters:
    #        if x not in dletters[lc]:
    #            dletters[lc].append(x)
    #        else:
    #            continue
    #    else:
    #        print('...')
    #        dletters[lc] = [x]
    #    print(dletters)

    #return min(dletters[max(dletters)])
    return max(string.ascii_lowercase, key=text.lower().count)
checkio = lambda t:max('abcdefghijklmnopqrstuvwxyz',key=t.lower().count)
if __name__ == '__main__':
    print(checkio('Abe!!!!'))
