# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:37:01 2019

@author: parth
"""

import random

def wordList():        
    words = ['India','Usa','Japan','China','England','Spain','Germany','Russia','Nepal','London']
    return random.choice(words).upper()

word = wordList()
word_letter = list(word)

def check(word,guessesNum,guess):
    status = ''
    matchLetter = 0
    for letter in word:
        if letter in guessesNum:
            status = status + letter
        else:
            status = status + "_ "
 
        if letter == guess:
            matchLetter = matchLetter + 1
   
    if matchLetter == 1:
        print ('You have guessed the letter correctly', guess )
    else:
        print ('The letter you enteres is not present in the word ')
    return status

def main():
   
    num_of_guess = 0
    guessesNum = []
    guessed = False
    test = '_ ' * len(word_letter)
    print ('The word is \"', test , '\" and it has ', len(word_letter),'letters!' )
    while not guessed:
        guess = input('please input a letter ')
        guess = guess.upper()
        if  len(guess) == 1:
            num_of_guess += 1 
            if guess in guessesNum:
                print ('This letter is already entered ',guess)
            elif len(guess) == 1: 
                guessesNum.append(guess)
                result = check(word, guessesNum, guess)
                if '_ ' not in result :
                    guessed = True 
                else:
                    print (result)
        else:
            print ('you should enter only 1 letter please enter again    ' )
    print ('Congratulation you found the the word: ', word ,' correctly in ',num_of_guess,'steps')  
main()
