#A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#by saksham madan

import math


#Recursive function to reverse the number
def rev(num): 
    res = str(num) == str(num)[::-1] 
    return res
    

#as the largest will always be in the nineties no need to run it for all the numbers
def largest():
    large = []
    arr = []
    for i in range(900, 1000):
        for j in range(900, 1000):
            arr.append(i*j)
    
    for i in arr:
        check = rev(i)
        if check == True:
            large.append(i)
    
    return max(large)


x = largest()

print(x)
