#It asks a range, then user will decide about a number and give feedbacks to the question
#MIN = int(raw_input("Enter the lower bound of the guess:"))
#MAX=  int(raw_input("Enter the upper bound of the guess:"))
MIN = 0
MAX = 100
print "Please think of a number between 0 and 100!"

Finished = False 
proper_input = False

while Finished == False: #when feedback is c, it will break the loop
    guess= (MAX+MIN)/2.
    print "Is your secret number" , guess , " ?"

    while proper_input == False :  #when feedback is h l or c, it will break the loop 
        print "Enter 'h' to indicate the guess is too high",
        print "Enter 'l' to indicate the guess is too low",
        print "Enter 'c' to indicate I guessed correctly."
        feedback = str(raw_input("Enter h, l or c:"))
        if (feedback != 'h') and (feedback != 'l') and (feedback != 'c'):
            print "Sorry, I did not understand your input."
            print "Is your secret number" , guess , " ?"
        else :
            break
          
    if feedback == 'c':
        break
    else :
        if feedback == 'h' :
            MAX = guess
        elif feedback == 'l' :
            MIN = guess
            
print "This is the best guess" , guess
