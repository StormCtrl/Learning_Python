'''
Readme / Notes
Finished the code for comparing user input & generated word.
Now I need to make a v2 of the "Geuss This Word"
'''
import random
#read an local txt file with all the words and import them into a global wordlist
def open_and_import_list():

    global importWordList
    importWordList = []

    f = open("wordlist.txt", "r")
    for x in f:
        importWordList.append(x)
        #print("Added: " + x)
    f.close()
    #print(importWordList) #Debugg: Check if everything is imported

#option to add more words to the file
def open_and_append_list():
    f = open("wordlist.txt", "a")
    add = input("Which word do you want to add to the database?: ")
    f.write(add)
    f.close()
    open_and_import_list()
    print("Added " + add + " and reloaded the list")

#function that puts individual letters in a list for comparison
def create_the_lists(x,y):
    global userguess
    global realguess
    userguess = []
    realguess = []
    x = str(x)
    y = str(y)
    for letter in x:
        userguess.append(letter)
    for letter in y:
        realguess.append(letter)

#function that compares both lists and returns a proper feedback so the player knows what he guessed right
def compare_list_and_feedback(x,y):
    global combinedguess
    combinedguess = []
    indexCounter = 0
    combined = ""

    #Check if the word is the same lenght, if not, it stops the function
    if len(x) != len(y):
        print("Not the same lenght! You wasted your guess")
        indexCounter = indexCounter + 1
    else:
        #Check which letter has been guessed correctly
        for letter in x:
            if letter in x[indexCounter] == y[indexCounter]:
                combinedguess.append(letter)
                indexCounter = indexCounter + 1
            else:
                combinedguess.append("_")
                indexCounter = indexCounter + 1

                #Make sure that the list becomes a full word again instead of list
    for letter in combinedguess:
        combined = combined + letter

    print(combined)

#the core of the game to start playing the game - MVP
def guess_this_word():

    #Base attributes
    wordlist = importWordList
    lenghtRandom = len(wordlist)
    randompick = random.randint(0,lenghtRandom)
    guess = wordlist[randompick].lower().replace("\n","")
    lenghtWord = len(guess)
    max = 10
    answer = " "
    counter = 10

    print("----------------------- DEBUGG: " + str(lenghtWord) + " " + guess)

    #Opening Message for a single round within the game
    print("The lenght of the word is " + str(lenghtWord) + "\nYou have " + str(max) + " chances to geuss it right\nGoodLuck\n.....")

    while answer != guess or counter != 0:
        print("You have " + str(counter) + " guesses left")
        answer = input("What word are you guessing?: ").lower()
        counter = counter - 1
        print("----------------------- DEBUGG: " + str(lenghtWord) + " " + guess)
        if counter == 0:
            print("You lost! You are out of guesses!")
            break
        if answer == guess:
            print("You won! Job well done!")
            break

#the core of the game, but version 2
def guess_this_word_v02():

    #Base attributes
    wordlist = importWordList
    lenghtRandom = len(wordlist)
    randompick = random.randint(0,lenghtRandom)
    guess = wordlist[randompick].lower().replace("\n","")
    lenghtWord = len(guess)
    max = 10
    answer = " "
    counter = 10

    #Opening Message for a single round within the game
    print("The lenght of the word is " + str(lenghtWord) + "\nYou have " + str(max) + " chances to geuss it right\nGoodLuck\n.....")

    while answer != guess or counter != 0:
        print("You have " + str(counter) + " guesses left")
        answer = input("What word are you guessing?: ").lower()
        counter = counter - 1

        #Give feedback to the player what they need to geuss the word
        create_the_lists(answer,guess)
        compare_list_and_feedback(userguess,realguess)

        if counter == 0:
            print("You lost! You are out of guesses!")
            break
        if answer == guess:
            print("You won! Job well done!")
            break

#game_loop so you can keep on playing
def game_loop():
    nrgame = 0
    keepPlaying = True
    while keepPlaying == True:
        getAnswer = input("Do you want to (continue) play this game? (y/n): ").lower()
        if getAnswer == "n":
            keepPlaying = False
        elif getAnswer == "y":
            nrgame = nrgame + 1
            print("Awesome! Lets play game number #" + str(nrgame))
            guess_this_word_v02()
        else:
            print("Not a proper answer! Please answer properly with a (y/n)")

open_and_import_list()
game_loop()
