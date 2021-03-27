from string import ascii_lowercase as lower
from string import ascii_uppercase as upper

size = len(lower)
message = 'Myxqbkdevkdsyxc, iye mbkmuon dro myno'

def caesar(message, shift):
    """ This function returns a caesar (substitution) cipher for a given string where numbers, 
    punctuation, and other non-alphabet characters were passed through unchanged. Letter case is 
    preserved.  """

    l_shift = {c:lower[(i+shift)%size] for i,c in enumerate(lower)}
    u_shift = {c:upper[(i+shift)%size] for i,c in enumerate(upper)}
    l_shift.update(u_shift)
    
    sf = [l_shift.get(c, c) for c in message]
    return ''.join(sf) 

print(caesar(message, 16))