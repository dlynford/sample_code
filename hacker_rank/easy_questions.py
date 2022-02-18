# 2/3/2022

# python if else problem: https://www.hackerrank.com/challenges/py-if-else/problem?h_r=next-challenge&h_v=zen

# Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird

n = int(input("Enter an integer: "))

if n % 2 != 0: #odd
    print("Weird")
if n % 2 == 0 and (n >= 2 and n <=5): #even
    print("Not Weird")
if n % 2 == 0 and (n >=6 and n <= 20): #even
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not Weird")
