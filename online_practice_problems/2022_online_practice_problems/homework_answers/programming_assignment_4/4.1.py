# 2/11/2022

# 1.	Write a program to print the following number pattern using a loop.

# result = ""
# for number in range(1, 6):
#     number = str(number)
#     result += f"{number} "
#     print(result)

# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 2/17/2022
# Alternate strategy:
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")

print("-"*9 + "*"*5)
print("-"*11 + "*"*7)
print("-"*9 + "*"*5)

for i in range(1,6):
    for j in range(i,6):
        print(j, end=" ")
    print("")