import random

wordlist = '..\\random_words.txt'

def get_word():
    num_words_processed = 0
    curr_word = None
    l = []
    with open(wordlist, 'r') as f:
        lines = f.readlines()

        for line in lines:
            l.append(line)
            num_words_processed+=1
        
        pick_num = random.randint(0, num_words_processed)
        curr_word = l[pick_num]
    return curr_word
        
