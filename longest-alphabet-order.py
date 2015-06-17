s = 'rstuwyabcdefghkl'

sort = ''
guessord = 0
longest = 0

for i in s :
    if ord(i) >= guessord:
        sort = sort + i
        if len(sort) > longest :
            longest = len(sort)
            result = str(sort)
    else :
        sort = i
    guessord = ord(i)
        

print "Longest substring in alphabetical order is:" , result        
