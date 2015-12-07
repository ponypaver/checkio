#! /usr/bin/env python

'''
Reverse each word
"Hello" ⇒ "olleH".
Swap letter case, uppercase to lowercase and versus.
"AsD" ⇒ "aSd".
Change each digit in numbers to the difference between 9 and the digit.
"140" ⇒ "859" (9-1=8, 9-4=5, 9-0=9).
Replace some punctuation symbols to each other with the follow list:
"," ⇔ "."
"!" ⇔ "?"
"(" ⇔ ")"
"{" ⇔ "}"
"[" ⇔ "]"
"<" ⇔ ">"
"@" ⇔ "#"
";" ⇔ ":"
Truncate several consecutive whitespaces in one.
"      " ⇒ " ".
There is one restriction however, to evade Stephens detection, your code should have no more than 12 lines with no more than 80 symbols in each line and "\t" will be counted as 4 symbols'''


import re

def twist(s):
    dd = dict(zip(',!({[<@;.?)}]>#:', '.?)}]>#:,!({[<@;'))
    for i,c in enumerate(s):
        if c in ',!({[<@;.?)}]>#:':
            s = s[:i] + dd[c] + s[i+1:]; 
        elif c.isdigit():
            s = s[:i] + chr(57 - int(c)) + s[i+1:]
    pos=0
    for w in re.compile('[a-zA-Z]{2,}').findall(s):
        pos += s[pos:].find(w)
        s = s[:pos] + w[::-1] + s[pos + len(w):]
    return re.sub( '\s+', ' ', s.swapcase())

def test():
   print(twist("Hello World!"))
   print(twist("I`m 1st"))
   print(twist("How are you? 905th."))
   print(twist("The code - ([{<;#>}])"))
   print(twist("EMAIL        a@b.ru"))
   print(twist(";-) 0_0 @__@"))
   print(twist("ab..BA"))
   print(twist("        ")+'.')
   print(twist("The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs!  Now fax quiz Jack!  my brave ghost pled. Five quacking zephyrs jolt my wax bed. Flummoxed by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed by MTV for luck. A wizard’s job is to vex chumps quickly in fog."))

if __name__ == '__main__':
    test()
