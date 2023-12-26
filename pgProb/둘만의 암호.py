def get_skip_alphalist(skip):
    skip = list(skip)
    arr = []
    for i in range(len(skip)):
        skip[i] = ord(skip[i])
    
    for i in range(97,123):
        if i in skip:
            continue
        arr.append(chr(i))
    
    return arr

def shift_alphabet(alphabet, index, skip_alphabet_list):
    skip_alpha_len = len(skip_alphabet_list)
    return skip_alphabet_list[(skip_alphabet_list.index(alphabet) + index) % skip_alpha_len]
        

def solution(s, skip, index):    
    alphabet_list = get_skip_alphalist(skip)
    
    shift_s = "".join([
        shift_alphabet(alphabet, index, alphabet_list) for alphabet in list(s)
    ])
    
    return shift_s
