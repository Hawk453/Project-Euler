#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#By Saksham Madan

# A function to print all prime factors of  
# a given number n 
import math

def primeFactors(n): 
    arr = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        arr.append(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            arr.append(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2:
        arr.append(n)

    return arr

n = 600851475143
arr = []
arr = primeFactors(n)

print(arr)

         