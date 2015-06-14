#example: 0.375 is a float and if we multiply it by 2**3, is equal to 3.0, the integer is 3, the binary for this integer 11
# then we need to shift it by 2**3 which will be 0.011
number = float(raw_input("Enter a number"))
if number < 0:     # if the number is negative, take the abs and remember that it was negative
    number = abs(number)
    isNeg=True
else:
    isNeg=False
##### First we need to make the decimal number a whole number
ndec = 0
while (number - int(number)) > 0 :
    number = number * 2
    ndec += 1
    print number
   
##### Now that we have the whole number we have to convert it to integer
number = int (number)
print ndec
##### And we compute the binary for that integer
binary=''
if number == 0 :
    binary = '0'
while number > 0:    # divide the number by 2 and take the remaining as the first binary on the right side 
    binary = str(number %2) + binary
    number = number/2  #replace the number by its half and continue 
        
##### Now if dec !=0 ... means the number was float and we have to correct the bianry for that
if ndec-len(binary) > 0 :
    for i in range (ndec-len(binary)) :
        binary = '0' + binary
    binary = binary[0:-ndec]+'.'+binary[-ndec:]
if isNeg == True :
    binary = '-' + binary
print binary    
