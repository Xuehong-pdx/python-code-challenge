""" The script aims to recover a lost passphrase based on two criteria: 

1) The pass phrase is composed of 3 to 6 of the following terms, in any order, separated by spaces:
espresso, latte, mocha, Arabica, dark roast, french press, pastry, cappuccino, jitters.
2) The encrypted file name contains part of hex-encoded SHA-256 hash of the pass phrase. 
With this information we know the sha256 sum of the pass phrase starts with 260fd51e 
"""

import hashlib
import itertools

ls = ['espresso', 'latte','mocha','Arabica','dark roast', 'french press', 'pastry','cappuccino','jitters']

# generate permutations with 3 to 6 items
pp=[]
for i in range(3,7):
    p = list(itertools.permutations(ls,i))
    pp.append(p)

# flateen the list of lists
pp = [item for p in pp for item in p]

# function to convert to hex
def to_hex(s):
    return hashlib.sha256(s.encode()).hexdigest()

for p in pp:
    jp = ''
    jp = ' '.join(p)
    hex_p = to_hex(jp)
    if hex_p[0:8] == '260fd51e':
        print("Bob's forgotten pass phrase is:", jp)
        break