number = float(raw_input("Enter an integer:"))
if number < 0:
    isNeg = True
else:
    isNeg = False
number = abs(number)
ans= 0.
nstep = 0
max_step =100000
epsilon = 0.01
step_size= epsilon **2

while (abs(number - ans**2) > epsilon) and (ans**2 <= number) :
       ans = ans + step_size
       nstep += 1
    
if isNeg == True :
    ans = -1 * ans 
print nstep, ans
