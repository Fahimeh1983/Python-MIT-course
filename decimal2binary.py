number = int(raw_input("Enter an integer:")) #take a number
if number < 0:     # if the number is negative, take the abs and remember that it was negative
    number = abs(number)
    isNeg=True
else:
    isNeg=False
    binary=''
    if number == 0 :
        binary = '0'
    while number > 0:    # divide the number by 2 and take the remaining as the first binary on the right side 
        binary = str(number %2) + binary
        number = number/2  #replace the number by its half and continue 
if isNeg == True:
    binary = '-' + binary
print binary
