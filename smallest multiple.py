#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#by saksham madan
import math

def lcm(n):  
    ans = 1
    for i in range(1, n + 1):  
        ans = int((ans * i)/math.gcd(ans, i))          
    return ans  

n = 20

x = lcm(n)

print(x)