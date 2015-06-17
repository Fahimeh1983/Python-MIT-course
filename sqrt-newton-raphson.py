# p = x**2 - number, we have to solve this equation
# ig g is an approxiamtion to the root, the next best guess
#is g- p(g)/p'(g)

number = float(raw_input("Enter an integer:"))
if number < 0:
    isNeg = True
else:
    isNeg = False
number = abs(number)

guess= number/2.
nstep = 0
epsilon = 0.01

while (abs(number - guess**2) > epsilon) :
       guess = guess - (guess**2 - number)/(2*guess)
       nstep += 1
    
if isNeg == True :
    ans = -1 * guess 
print "After ", nstep, "steps, my best guess if: ", guess
