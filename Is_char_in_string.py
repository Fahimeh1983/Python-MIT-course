#Check if a character is in inside an string (alphabetically ordered already)

def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and char != aStr :
        return False 
    else:
        mid = aStr[len(aStr)/2]
        if char == mid:
            return True
        elif char < mid:
            return len(aStr[0:len(aStr)/2]) != 0 and isIn(char,aStr[0:len(aStr)/2])
        else:
            return len(aStr[len(aStr)/2:]) != 0 and isIn(char,aStr[len(aStr)/2:])
