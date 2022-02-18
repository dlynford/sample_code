# 2/16/2022
# 5.	Write a program to print the cube of all numbers from 1 to a given number

a = int(input("Enter a positive integer to be cubed: "))
while a < 1:
    a = int(input("Please enter a positive integer: "))
cubes = [i**3 for i in range(1, a+1)]
# print(cubes)
for count, cube in enumerate(cubes, 1):
    print(f"Count {count}: {cube}")
