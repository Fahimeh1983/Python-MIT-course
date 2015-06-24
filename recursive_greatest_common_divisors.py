A clever mathematical trick that makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    lower = min (a,b)
    upper = max (a,b)
    if lower == 0 :
       return upper 
    else : 
       return gcdRecur (lower , upper % lower)

