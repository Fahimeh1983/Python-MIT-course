number = float(raw_input("Enter an integer:"))
if number < 0:
    isNeg = True
else:
    isNeg = False
number = abs(number)

MAX= number
MIN= 0
guess= (MAX+MIN)/2. 
nstep = 0
epsilon = 0.01

while (abs(number - guess**2) > epsilon) :
    if (guess**2 < number):
        MIN = guess
    else:
        MAX = guess
    guess = (MAX+MIN)/2. 
    nstep += 1
    
if isNeg == True :
    ans = -1 * guess 
print "After ", nstep, "steps, my best guess if: ", guess
