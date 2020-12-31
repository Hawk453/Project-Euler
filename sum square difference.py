#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def sum_individual():

    arr = []
    for i in range(1, 101):
        arr.append(i*i) 
    
    sum = 0
    for i in arr:
        sum = sum + i

    return sum

def sum_collective():

    sum  = 0
    for i in range(1, 101):
        sum = sum + i

    return sum*sum


a = sum_collective() - sum_individual() 
print(a)