def isPalendrom(s):
    def toChar(s):
        s = s.lower() # Make it all lower case
        result = ''   # If there are some other string such as , / ? remove them 
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                result = result + char
        return result
        
    def isPal(s):
        if len(s) == 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
            
    return isPal(toChar(s))
    
print isPalendrom("A r i r...a")
