#this is a brute force method

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#by saksham madan
n = 1000000000
arr = []
for i in range(1, n):
    if i%1 == 0 and i%2 == 0 and i%3 == 0 and i%4 == 0  and i%5 == 0  and i%6 == 0  and i%7 == 0  and i%8 == 0  and i%9 == 0  and i%10 == 0 and i%11 == 0 and i%12 == 0 and i%13 == 0 and i%14 == 0  and i%15 == 0  and i%16 == 0  and i%17 == 0  and i%18 == 0  and i%19 == 0  and i%20 == 0:
        arr.append(i)

print(arr)