#Example of tuple

def Find_divisor(a,b):
    if a == 0 :
        return b
    elif b == 0 :
        return a
    else :
        result=() #empty tuple
        for i in range(1,min(a,b)+1):
            if a % i == 0 and b % i == 0:
                result = result + (i,) #adding to tuple
        return result
        
print Find_divisor(20,100)
