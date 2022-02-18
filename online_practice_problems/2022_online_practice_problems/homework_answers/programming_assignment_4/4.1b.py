for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")

for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=" ")
    print("")

# output:
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5



# for i in reversed(range(1, 6)):
#     # print(i)
#     for number in range(i,6):
#         print(number, end=" ")
#     print("")

# output:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5