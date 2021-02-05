import os
import sys
import keyboard
from word import get_word

class word:
    def __init__(self, word, chance, length):
        self.word = word
        self.chance = chance
        self.length = length
        self.list_word = list
    
    def get_word(self):
        return self.word

    def get_chance(self):
        return self.chance

    def get_length(self):
        return self.length

    def dec_chance(self):
        self.chance -= 1

    def try_answer(self, answer):
        if self.word == answer:
            return True
        else:
            return False

    def try_alpha(self, alpha):
        if alpha in self.word:
            return True
        else:
            return False

def main_page():
    os.system('cls')
    print("Welcome to Hangman Game.\n")
    print("=============================================================================\n")
    print("How to Play:")
    print("1. You will given a random words.")
    print("2. Based on the length of the word, you will given certain amount of chance.")
    print("3. With that certain amount of chance, you have to guess the word.\n")
    print("Press Enter to Start Game.")
    print("Press 'q' to Exit the Game.\n")
    print("=============================================================================")

while True:
    main_page()

    while True:
        key = input()

        if key == "":
            break
        elif key == "q":
            sys.exit()
        else:
            main_page()
            print("Please press Enter or q.", end = '')

    temp = get_word().strip()
    temp = temp.lower()
    d = {}
    length = len(temp)
    chance = int(length * 1.5)
    for i in range(len(temp)):
        d[temp[i]] = False
    w_obj = word(temp, chance, length)
    win = False
    count = 0

    while True:
        if win == True: break
        if w_obj.get_chance() == 0:
            os.system('cls')
            print("You lose")
            print("Press Enter to go back to main page")
            n = input()
            if n == "":
                break
            
        os.system("cls")
        print("\n\n                             Hang Man                                \n\n")
        print("=============================================================================\n")
        print("You have {0} chances left.\n\n\n".format(w_obj.get_chance()))
        print("",end = '   ')
        for i in range(length):
            if d[temp[i]] == True:
                print(temp[i], end=" ")
            else:
                print("_", end = " ")
        print("\n\n")
        print("=============================================================================\n")
        

        print("Type any alphabet or whole word if you find out the answer.")
        n = input()
        if len(n) > 1:
            ans = w_obj.try_answer(n)
            if ans == True:
                os.system('cls')
                print("You Win!!")
                win = True
                n = input("Press Enter to go back to main page")
            else:
                w_obj.dec_chance()
                print("Try Again!")
        else:
            ans = w_obj.try_alpha(n)
            if ans == True:
                d[n] = True
                count += 1
                if count == len(d):
                    os.system('cls')
                    print("You Win!!")
                    win = True
                    n = input("Press Enter to go back to main page")
            else:
                w_obj.dec_chance()
                print("Try Again!")

    
    