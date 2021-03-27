"""  This program reads in a lexicon file of valid dictionary words. It then accepts a player's rack
of letters (a list size 1-10) and produces the top N playable words based on scrabble score.  
A word is considered playable only if it is contained in the lexicon and all letters required to 
form the word are in the supplied rack.  """

import urllib.request
import itertools

url = 'https://raw.githubusercontent.com/PDXPythonPirates/code-challenges/master/03-scrabble-words/sowpods.txt'
    
def import_file(url):
    
    file = urllib. request. urlopen(url)
    word_dict = set()
    for line in file:
        decoded_line = line. decode("utf-8").rstrip()
        word_dict.add(decoded_line)
    return word_dict

# assign score to charaters based on convention
score_dic = {'A': 1,'B': 3,'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,'I': 1,'J': 8,'K': 5,
 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,'Q': 10, 'R': 1, 'S': 1,'T': 1,'U': 1, 'V': 4,
 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

def get_inputs():
    inputs = input("Enter 1-10 letters separated by spaces: ").upper()
    return list(inputs.split())

# generate unique words based on entered characters that are in the work_dict
def prep_list(input_letters, word_dict):
    play_words = []
    for i in range(1, len(input_letters)+1):
        l_perm = list(itertools.permutations(letters, i))
        unique_words = list( set( [''.join(x)for x in l_perm] ) )
        words_ls = [x for x in unique_words if x in word_dict]
        play_words.append(words_ls)
    play_words = [x for sub in play_words for x in sub]
    
    # generate character lists for each selected word
    char_ls = []
    if play_words:
        for w in play_words:
            char_ls.append([char for char in w ])
        return char_ls
    else:
        print("Word not in dictionary.")
        return None

# score each words based on character scores 
def word_rank(char_ls, score_dic):
    
    if char_ls is None:
        return None
    else:
        word_score = []
        for sub in char_ls:
            score=0
            for c in sub:
                score += score_dic.get(c)
            word = ''.join(sub)
            w_s = (word, score)
            word_score.append(w_s)
        return sorted(word_score, key = lambda x: x[1], reverse = True)

word_dict = import_file(url)
letters = get_inputs()
char_ls = prep_list(letters, word_dict)
top_ls = word_rank(char_ls, score_dic)[0:10]
print('Your top playable words and their scores are: ', top_ls)