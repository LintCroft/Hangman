'''
Created on 9 Sept 2014

@author: james.browning
'''

from functions import check_letter,get_word,scoring,load_on_startup,save_on_exit


#Intro message and load game
print("Welcome to the Hangman game")
load_game = input("Would you like to load a saved game?\n > ")

if load_game == 'y' or load_game == 'yes':
    name,score,round_count = load_on_startup()
    
    print("Welcome back {}. Your score is {}/{}".format(name,score,round_count))
else:
    score = 0
    round_count = 0

used_letters = []

#MainGame, can be restarted
while True:
    tries = 10
    round_count += 1
    word = get_word()
    word_list = list(word)
    answer = []
    
    for letter in word_list:
        answer.append("_") 
    
    print(' '.join(answer))
    print("\nGuess a letter")
    guess = input("> ").lower()
    
    while tries > 0 and "_" in answer and  guess != "give up":
        if guess.isdigit():
            print("Please use letters only")
            guess = input("> ").lower()
        elif len(guess) > 1:
            print("Please only guess one letter")
            guess = input("> ").lower()
        elif len(guess) <1:
            print("Please guess a letter")
            guess = input("> ").lower()
        elif guess in used_letters:
            print("You have already tried that one")
            guess = input("> ").lower()
        else:
            used_letters.append(guess)
            tries = check_letter(word_list,guess,answer,tries)
            if tries > 0 and "_" in answer:
                print("\nYou have {} tries remaining".format(tries))
                print(' '.join(answer))
                print("\nLetters used: {}".format(' '.join(used_letters)))
                print("Guess another letter")
                guess = input("> ").lower()
            else:
                break
    
    if '_' not in answer:
        print("\nCongratulations")
        win = True
        score = scoring(win,score,)
        print ("The answer was'{}'. Your score is {}/{}".format(word,score,round_count))
    else:
        print("\nGAME OVER\n")
        win = False
        score = scoring(win,score,)
        print ("The answer was'{}'. Your score is {}/{}".format(word,score,round_count))
    
    if input("\nWould you like to play again? ") == 'y':
        print("\n")
        continue
    else:
        save_on_exit(score,round_count)
        print("Bye.")
        break