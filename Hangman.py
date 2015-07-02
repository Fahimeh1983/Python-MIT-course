import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    countcorrect = 0
    for l1 in secretWord :
         for l2 in lettersGuessed:
                if l1 == l2 :
                    countcorrect += 1
                    break
    if countcorrect == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    guessed = ""
    for l1 in secretWord:
        if l1 in lettersGuessed  :
            guessed = guessed + l1
        else :
            guessed = guessed + "_ "   
    return guessed

def getAvailableLetters(lettersGuessed):
    remain = ""
    for l1 in string.lowercase[:]:
        if l1 not in lettersGuessed:
            remain = remain + l1
    return  remain 

def letterinWord(secretWord,newletter):
    secretlist = list(secretWord)
    return len(set(secretlist).intersection(newletter)) > 0

def alreadyguessed(lettersGuessed,newletter):
    return len(set(newletter).intersection(set(lettersGuessed))) > 0


def hangman(secretWord):
    lettersGuessed = []
    correctGuessed = []
    n_guess = 8
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(secretWord),"letters long."

    while 0 < n_guess <= 8 :
        print "-----------"
        print "You have",n_guess,"guesses left"
        print "Available Letters:", getAvailableLetters(lettersGuessed)
        letter = [raw_input("Please guess a letter:")] 
        newletter = [x.lower() for x in letter]
        
        if alreadyguessed(lettersGuessed,newletter): 
            lettersGuessed = lettersGuessed + newletter
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)    
        elif letterinWord(secretWord,newletter):
            lettersGuessed = lettersGuessed + newletter
            print  "Good guess:" , getGuessedWord(secretWord, lettersGuessed)
            correctGuessed = correctGuessed + newletter
            if isWordGuessed (secretWord,correctGuessed) == True :
                 print "-----------"
                 return "Congratulations, you won!" 
        else:
            lettersGuessed = lettersGuessed + newletter
            print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
            n_guess -= 1
    print "-----------"        
    return "Sorry, you ran out of guesses. The word was %s." % secretWord 
        
              
wordlist = loadWords()
secretWord = chooseWord(wordlist)        
print hangman("c")
