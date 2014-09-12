'''
Created on 9 Sep 2014

@author: james.browning
'''
#This function checks whether the guessed letter is in the word
def check_letter(word_list,guess,answer,tries):
    n = -1
    correct = False
    #for each letter in the word it checks whether the guessed letter is there
    for letter in word_list:
        if guess == letter:
            correct = True #If the guessed letter occurs at least once then the player is correct
            n += 1
            answer[n] = guess #The letter is 'revealed' by adding to the answer list
        else:
            n += 1
    #function prints a message and then returns the number of tries      
    if correct:
        print("Well Done")
        return tries
    else:
        print("Bad Luck")
        tries -= 1 #Tries remaining goes down by one if wrong answer
        return tries 
        
#This function gets a random word from the words.txt file        
def get_word():
    import random
    word_choice = []
    with open('words.txt','r') as w: #Opens the words.txt file with read permissions
        for line in w: #for each line it takes the word and puts it in a list
            line = line.rstrip('\n')
            word_choice.append(line)
    
    choice = random.randint(0,len(word_choice)-1) #Now a word is selected at random
    return word_choice[choice].lower() #Random word is returned

#This function simply adds to the score count when the player wins a round
def scoring(win,score):
    if win:
        score += 1
    return score

# This functions loads a saved game from save.csv, one of two slots is loaded
def load_on_startup():
    import csv
        
    row_list = []
    with open('save.csv', 'rt') as csvfile: #save.csv file is opened with read permissions
        read_save = csv.reader(csvfile, delimiter=' ') #delimiter is the separator between fields 
        for row in read_save: #for each row (there should only be 2) it will add the info into row_list 
            row_list.extend(row)
                    
    print("Slot 1: {}\nSlot 2: {}".format(row_list[0],row_list[3])) #Prints the names of the previous players saved games
    slot = int(input("Which slot would you like to load from, 1 or 2?")) #Player chooses a slot to load
    
    #Relative information is extracted from row_list depending on which slot the player chose
    if slot == 1:
        name = row_list[0]
        score = int(row_list[1])
        round_count = int(row_list[2])
    elif slot == 2:
        name = row_list[3]
        score = int(row_list[4])
        round_count = int(row_list[5])
            
    return name,score,round_count #The extracted information is returned

# This function saves a game into save.csv
def save_on_exit(score,round_count):
    import csv
    save = input("Would you like to save your score?\n> ").lower() #PLayer is asked whether they want to save the game
    if save == "y" or save == "yes":
        row_list = []
        with open('save.csv', 'rt') as csvfile: #save.csv is opened with read permissions
            read_save = csv.reader(csvfile, delimiter=' ') #delimiter is the separator between fields 
            for row in read_save: #for each row (there should only be 2) it will add the info into row_list 
                row_list.extend(row)
                
        print("Slot 1: {}\nSlot 2: {}".format(row_list[0],row_list[3])) #Prints the names of the previous players saved games
        slot = int(input("Which slot would you like to save to, 1 or 2?")) #Player chooses a slot to save to
        
        same_name = input("Would you like to rename the slot?").lower() #Ask player if they wish to rename the save slot
        if same_name == 'y' or same_name == 'yes':
            player_name = input("Please input your name\n> ")
        elif slot == 1:
            player_name = row_list[0] #If player doesn't want to rename then player_name is set same as previous save
        elif slot == 2:
            player_name = row_list[3] 
        
        with open('save.csv', 'wt') as csvfile: #save.csv is opened with write permissions
            write_save = csv.writer(csvfile, delimiter=' ') #delimiter is the separator between fields 
            if slot == 1:
                write_save.writerow([player_name,score, round_count]) #writes player name with current score and round_count
                write_save.writerow([row_list[3],row_list[4],row_list[5]]) #writes the other slot so data isn't lost
            elif slot == 2:
                write_save.writerow([row_list[0],row_list[1],row_list[2]])
                write_save.writerow([player_name,score, round_count])
        
        
        print("Saved")