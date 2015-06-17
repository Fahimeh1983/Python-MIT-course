s = 'rstuwyabcdefghkl'
# s is an example
sort = '' 
guessord = 0 # all the alphabetical orders are above 90
longest = 0  # the longest one has a length of zero

for i in s :
    if ord(i) >= guessord:
        sort = sort + i   # if the order of the next char is more than the previous one, it will be added to our string
        if len(sort) > longest :
            longest = len(sort)
            result = str(sort)
    else :
        sort = i  # if the order of rht next char is less than the previous one, the string will restart
    guessord = ord(i)
        

print "Longest substring in alphabetical order is:" , result        
