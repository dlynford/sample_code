# 2/14/2022

# total = 0
# for i in range(0, 1_000_000):
#     total += i
# print(total)
#
# print(sum((i for i in range(0, 100_000_000))))

# q1:
# Q1- Display the message “I love python” 12 times using a loop. [HINT: use while loop]

#
# i = 1
# while i < 13:
#     print(i,"I love Python.")
#     i += 1

# for i in range(1, 13):
#     print(i, "I love Python.")

# q2:Q2- Prompt the user with the message “How many times do you want your loop to run”
# and store the result of what they type in a variable. Your program will loop however
# many times the user has requested using a while loop. Each time through the loop,
# your program will display the message “Still in a loop!”.
# It will also output a number indicating how many times the loop body has executed so
# far (the message and number should all appear on the same line).
# When the loop is finished, it will display “Okay! Bye!” [HINT: use for loop]

# n = int(input("How many times do you want your loop to run? "))
# i = 1
# while i < n + 1:
#     print(i, "Still in a loop!")
#     i += 1
# print("Okay!, Bye!")

#
# Q3- Create a program that prompts the user for an integer.
# Your program will use a while loop to count down from that number to one. [HINT: use while loop]

# b = int(input("Enter a number to countdown: "))
# while b >= 5:
#     print(b)
#     b -= 1
# print("End.")

# q4- Write a program to compare two number, store those number in variables and display
# the one that is greater. [HINT: use if-else]

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
#
# if a == b:
#     print(f"{a} is equal to {b}.")
#
# elif a > b:
#     print(f"{a} is greater than {b}.")
#
# else:
#     print(f"{b} is greater than {a}.")

# Q5- Write a program to compare two number, take the numbers as float input from the user and
# store those number in variables. Display the one that is greater. [HINT: use if-else]

# a = float(input("Number one: "))
# b = float(input("Number two: "))
#
# if a == b:
#     print("The numbers are equal.")
#
# elif a > b:
#     print(f"{a} > {b}")
#
# else:
#     print(f"{a} < {b}")

# Q6- Write a program to display the smallest number in a list. [HINT: List]
# numbers = list(range(1, 11))
# # print(numbers)
#
# Q7- Write a program to perform following steps on the list:
# 1.	Create a list
# 2.	Display the original list
# 3.	Change an element in the list
# 4.	Add ONE element to the list
# 5.	Add THREE elements together to the list
# 6.	Display the final list.
# a = int(input("Enter an integer to build a list: "))
# new_list = list(range(1, a +1))
# print(new_list)
# new_list[4] = "Shanks"
# new_list.append("word")
# print(new_list)
# new_list.append("changes")
# new_list[0] = 333
# new_list[1] = 434
# print(new_list)
#
#
# print(new_list)


# i = 0
# a = "Hi Aeendreeeeewe"
#
# while (i<len(a)):
#     if a[i] == "e":
#         i+=1
#         continue
#     #print(i)
#     print(i, "->",a[i])
#     i+=1
#
#
# count = 0
# name = "Georgia O'Keefe"
# print(len(name))
#
# while 0 < 15: #while true proceed. When false, stop.
#      if  """if True proceed with this line of code. If False, skip this line and go to the next statement."""
#         print("whatever you want.")
#         0 + 1= 1 #add to the count here so you don't got through an infinite loop!
#         # continue pushes python to the next line of code
#     else:
#     print(" print the count, and the next letter in the word.")
#     # 0 + 1 = 1 add 1 to the count here or the loop becomes infinite.
#     #return to the beggining of the while loop at the top.
#     #repeat this process until the while loop evaluates to false.

# while count < (len(name)):
#     if name[count] == "e":
#         print(count, "-")
#         count += 1
#         continue
#     print(count, name[count])
#     count += 1
