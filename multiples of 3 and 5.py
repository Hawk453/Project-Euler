#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#By Saksham Madan
n = 1000
arr = []

for i in range(n):
    if i%5 == 0 or i%3==0:
        arr.append(i)
    

sum = 0
for i in arr:
    sum = sum + i



print(sum)
