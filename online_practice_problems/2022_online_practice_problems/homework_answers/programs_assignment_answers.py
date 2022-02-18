# 2/1/2022

# Question 1:
# count = 1
# while count <= 12:
#     print(count, "I love Python")
#     count += 1

# Question 2:
# ask = int(input('How many times do you want your loop to run?: '))
# for variable in range(1, ask+1):
#     print(variable, "Still in a loop")
# print("Ok bye!")

# Question 3: ??? This confuses me. Shouldn't the first or last number be excluded???
# integer = int(input("Enter a positive integer to count down between 5 and 25: "))
# while integer > 1:
#     for i in range(integer):
#         print(integer)
#         integer -= 1
# print("Done.")

# Question 4:
# Write a program to compare two number,
# store those number in variables and display the one that is greater. [HINT: use if-else]

# print("""
# Compare the value of two numbers below.
# (The larger one will be printed separately.)""")
# numbers = []
# number = int(input("\nEnter the first number: "))
# numbers.append(number)
# number = int(input("Enter the second number: "))
# numbers.append(number)
# # print(numbers, type(numbers))
#
# if numbers[0] == numbers[1]:
#     print(f"{numbers[0]} == {numbers[1]}.")
#     print("They are equal.")
# elif numbers[0] > numbers[1]:
#     print(f"{numbers[0]} > {numbers[1]}.")
#     print(f"{numbers[0]}")
# else:
#     print(f"{numbers[0]} < {numbers[1]}.")
#     print(f"{numbers[1]}")

# Question 5:
# Q5- Write a program to compare two number, take the numbers as float input from the
# user and store those numbers in variables. Display the one that is greater.

# message = """
# Enter two float numbers and compare them below.
# The greater one will be printed out.\n """
# print(message)
# floats = []
#
# new_float = float(input("Enter float number one: "))
# floats.append(new_float)
# new_float = float(input("Enter float number two: "))
# floats.append(new_float)
# # print(floats, type(floats))
# print(max(floats))

# Answer 5.2:
# message = """
# Enter two float numbers and compare them below.
# (The greater value will be printed out.)\n """
# print(message)
#
# x = float(input("Enter float number one: "))
# y = float(input("Enter float number two: "))
#
# if x == y:
#     print("\nThe values are equal.")
#     print(f"{x} == {y}.")
# elif x > y:
#     print(f"\n{x}")
# else:
#     print(f"\n{y}")


# Question 6: ??? Is there another way to do this problem using the list method???
# integers = []
# for i in range(1, 26):
#     integers.append(i)
# print(integers)
# print(min(integers))

# Question 7:
# - Write a program to perform following steps on the list:
# 1.	Create a list
# 2.	Display the original list
# 3.	Change an element in the list
# 4.	Add ONE element to the list
# 5.	Add THREE elements together to the list
# 6.	Display the final list.

# city = input("What city or town were you born in? ")
# city_list = list(city)
# print(city_list)
# # length = len(city_list)
# # print(length)
# city_list[0] = city_list[0].upper() # change one element
# city_list.append("_A_ ") # add one item.
# print(city_list)
# three_letters = ["_B_", "_C_", "_D_"] # add three items.
# city_list.extend(three_letters)
# print(city_list)

# output:
# What city or town were you born in? boston
# ['b', 'o', 's', 't', 'o', 'n']
# ['B', 'o', 's', 't', 'o', 'n', '_A_ ']
# ['B', 'o', 's', 't', 'o', 'n', '_A_ ', '_B_', '_C_', '_D_']