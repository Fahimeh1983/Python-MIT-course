#It asks a range, then user will decide about a number and give feedbacks to the question
MIN = int(raw_input("Enter the lower bound of the guess:"))
MAX=  int(raw_input("Enter the upper bound of the guess:"))

Finished = False 
proper_input = False

while Finished == False: #when feedback is c, it will break the loop
    guess= (MAX+MIN)/2.
    print "My guess is:" , guess

    while proper_input == False :  #when feedback is h l or c, it will break the loop 
        print "Is my guess correct?:" , guess
        feedback = str(raw_input("Enter h, l or c:"))
        if (feedback == 'h') or (feedback == 'l') or (feedback == 'c'):
            break
          
    if feedback == 'c':
        break
    else :
        if feedback == 'h' :
            MAX = guess
        elif feedback == 'l' :
            MIN = guess
            
print "This is the best guess" , guess
