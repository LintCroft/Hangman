'''
Created on 9 Sep 2014

@author: james.browning
'''
def check_letter(word_list,guess,answer,tries):
#    global tries
    n = -1
    correct = False
    
    for letter in word_list:
        if guess == letter:
            correct = True
            n += 1
            answer[n] = guess
        else:
            n += 1
            
    if correct:
        print("Well Done")
        return tries
    else:
        print("Bad Luck")
        tries -= 1
        return tries 
        
        
def get_word():
    import random
    word_choice = []
    with open('words.txt','r') as w:
        for line in w:

            line = line.rstrip('\n')
            word_choice.append(line)
    
    choice = random.randint(0,len(word_choice)-1)
    return word_choice[choice]


def scoring(win,score):
    if win:
        score += 1
    return score

def load_on_startup():
    import csv
        
    row_list = []
    with open('save.csv', 'rt') as csvfile:
        read_save = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in read_save:
            row_list.extend(row)
                    
    print("Slot 1: {}\nSlot 2: {}".format(row_list[0],row_list[3]))
    slot = int(input("Which slot would you like to load from, 1 or 2?"))
    
    if slot == 1:
        name = row_list[0]
        score = int(row_list[1])
        round_count = int(row_list[2])
    elif slot == 2:
        name = row_list[3]
        score = int(row_list[4])
        round_count = int(row_list[5])
            
    return name,score,round_count

def save_on_exit(score,round_count):
    import csv
    save = input("Would you like to save your score?\n> ").lower()
    if save == "y" or save == "yes":
        row_list = []
        with open('save.csv', 'rt') as csvfile:
            read_save = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in read_save:
                row_list.extend(row)
                
        print("Slot 1: {}\nSlot 2: {}".format(row_list[0],row_list[3]))
        slot = int(input("Which slot would you like to save to, 1 or 2?"))
        
        same_name = input("Would you like to rename the slot?")
        if same_name == 'y' or same_name == 'yes':
            player_name = input("Please input your name\n> ")
        elif slot == 1:
            player_name = row_list[0]
        elif slot == 2:
            player_name = row_list[3] 
        
        with open('save.csv', 'wt') as csvfile:
            write_save = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if slot == 1:
                write_save.writerow([player_name,score, round_count])
                write_save.writerow([row_list[3],row_list[4],row_list[5]])
            elif slot == 2:
                write_save.writerow([row_list[0],row_list[1],row_list[2]])
                write_save.writerow([player_name,score, round_count])
        
        
        print("Saved")