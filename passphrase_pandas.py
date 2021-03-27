""" The script aims to recover a lost passphrase based on two criteria: 

1) The pass phrase is composed of 3 to 6 of the following terms, in any order, separated by spaces:
espresso, latte, mocha, Arabica, dark roast, french press, pastry, cappuccino, jitters.
2) The encrypted file name contains part of hex-encoded SHA-256 hash of the pass phrase. 
With this information we know the sha256 sum of the pass phrase starts with 260fd51e 
"""

# importing libraries
import hashlib 
import itertools
import pandas as pd

# list of potential pass phrase terms
ls = ['espresso', 'latte','mocha','Arabica','dark roast', 'french press', 'pastry','cappuccino','jitters']

# using permutation to generate a list of all possible combos of the terms
pp = list(itertools.permutations(ls))

# store permutation results in dataframe df
df = pd.DataFrame(pp, columns = ['p1', 'p2','p3','p4','p5','p6','p7','p8','p9'])

# combine contents for three to six columns
df['pp3'] = df[df.columns[0:3]].apply(lambda x: ' '.join(x),axis=1)
df['pp4'] = df[df.columns[0:4]].apply(lambda x: ' '.join(x),axis=1)
df['pp5'] = df[df.columns[0:5]].apply(lambda x: ' '.join(x),axis=1)
df['pp6'] = df[df.columns[0:6]].apply(lambda x: ' '.join(x),axis=1)

# define a function to convert str to hex
def to_hex(s):
    return hashlib.sha256(s.encode()).hexdigest()

# coverting terms to passphrases
df['pp3_hx'] = df.pp3.apply(lambda x: to_hex(x))
df['pp4_hx'] = df.pp4.apply(lambda x: to_hex(x))
df['pp5_hx'] = df.pp5.apply(lambda x: to_hex(x))
df['pp6_hx'] = df.pp6.apply(lambda x: to_hex(x))

# generate test column to store True and False values 
# based on wether the hex string starts with '260fd51e'

df['pp3_test'] = df['pp3_hx'].str.startswith('260fd51e')
df['pp4_test'] = df['pp4_hx'].str.startswith('260fd51e')
df['pp5_test'] = df['pp5_hx'].str.startswith('260fd51e')
df['pp6_test'] = df['pp6_hx'].str.startswith('260fd51e')

# check True and False counts
print(df['pp3_test'].value_counts(), '\n')
print(df['pp4_test'].value_counts(), '\n')
print(df['pp5_test'].value_counts(), '\n')
print(df['pp6_test'].value_counts(), '\n')

# only passphrases contains four terms contains True values
df1 = df[df['pp4_test']==True]
print("Bob's forgotten pass phrase is:", df1.iloc[0, 10])
