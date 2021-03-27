""" The code below reads in the collective works of William Shakespeare found at
https://www.gutenberg.org/files/100/100-0.txt and prints out the top N most frequently 
occurring words. The stop words defined by nltk are ignored in the counts """

import re
N = int(input("How many top words would you like to know? "))
stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}

# read in files and create a collection of words, excluding stop words.
lines=[]
with open('/home/xueho/data/shakespeare.txt', 'r') as file:
    line_gen = (line for line in file)
    for line in line_gen:
        l = line.split()
        if l: 
            lines.append(l)

word_collection = [re.sub(r'[^a-zA-Z0-9]', '', w).lower() for sub in lines for w in sub] 
word_collection = [w for w in word_collection if w not in stop_words]

# calculate word frequecies
top_w = {}
for w in word_collection:
    if w in top_w:
        top_w[w] += 1
    else:
        top_w[w] = 1

# find top words the frequecy of usage.    
top_words = [(w,f) for w,f in top_w.items()]
top_words = sorted(top_words, key = lambda x: x[1], reverse=True)
print(f'The top {N} words are: ', top_words[0:N])