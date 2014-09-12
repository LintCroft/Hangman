'''
Created on 9 Sept 2014

@author: james.browning
'''
#Import functions from functions.py
from functions import check_letter,get_word,scoring,load_on_startup,save_on_exit


#Intro message and load game
print("Welcome to the Hangman game")
load_game = input("Would you like to load a saved game?\n > ")
#PLayer decides to load a previously saved game, choice of 2 slots
if load_game == 'y' or load_game == 'yes':
    name,score,round_count = load_on_startup()
    #Plater is welcomed back, displays previous score and round count
    print("Welcome back {}. Your score is {}/{}".format(name,score,round_count))
#if player decides not to load then default score and round count are used
else:
    score = 0
    round_count = 0

#MainGame, While can be restarted once round is over
while True:
    tries = 10 #Number of 'lives' a player has
    used_letters = [] #Already played letters
    round_count += 1 #Increment the round_count to aid scoring
    word = get_word() #Use get_word() function to read words.txt and randomly select a word
    word_list = list(word) #Converts the word string into a list
    answer = []#Blank answer list
    
    #add "_" to the answer list, in place of each character in the word
    for letter in word_list:
        answer.append("_") 
    #Prints the number of '_' as a string followed by prompt for player to guess a letter
    print(' '.join(answer))
    print("\nGuess a letter")
    guess = input("> ").lower()
    #Player must guess a single letter otherwise an error is displayed, also not one that has already been tried
    while tries > 0 and "_" in answer and  guess != "give up":
        if guess.isdigit(): #checks if input is a number
            print("Please use letters only")
            guess = input("> ").lower()
        elif len(guess) > 1: #checks if input is more than 1 character length
            print("Please only guess one letter")
            guess = input("> ").lower()
        elif len(guess) <1: #checks if there are no characters input
            print("Please guess a letter")
            guess = input("> ").lower()
        elif guess in used_letters: #checks if letter has been guessed before
            print("You have already tried that one")
            guess = input("> ").lower()
        else: #If all is ok it adds the guessed letter to the list of used letters
            used_letters.append(guess)
            tries = check_letter(word_list,guess,answer,tries)
            if tries > 0 and "_" in answer: #if there are more to guess then the round continues
                print("\nYou have {} tries remaining".format(tries))
                print(' '.join(answer))
                print("\nLetters used: {}".format(' '.join(used_letters)))
                print("Guess another letter")
                guess = input("> ").lower()
            else:
                break #If there are no more letters to guess, player runs out of tries or types "give up" then the round ends
    
    if '_' not in answer: #If there are no more letters to guess then the player has won
        print("\nYou Win!")
        win = True
        score = scoring(win,score,)
        print ("The answer was'{}'. Your score is {}/{}".format(word,score,round_count))
    else: #If there are still letters to guess then the player has obviously lost
        print("\nYou Lose\n")
        win = False
        score = scoring(win,score,)
        print ("The answer was'{}'. Your score is {}/{}".format(word,score,round_count))
    #Player is asked to play again, loop is re-started
    if input("\nWould you like to play again? ") == 'y':
        print("\n")
        continue
    else: #When game is exited the user can save their progress to one of two slots
        save_on_exit(score,round_count)
        print("Bye.\n")
        break