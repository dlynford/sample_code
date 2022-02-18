# 2/8/2022
# nested list problems from hacker rank.com
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# records = [
#     ["john", 75],
#     ["paul", 67],
#     ["george", 82],
#     ["ringo", 51],
# ]

# for i in range(4):
#     print(i)
# score_list = []

# for record in records:
#     # print(record[1])
#     score_list.append(record[1])
# print(score_list)

# sorted_list = sorted(score_list)
"""score_list.sort()
print(score_list)

# print(min(score_list))
# print(max(score_list))
second_lowest = score_list[1]
print(second_lowest)
"""

# records = [
#     ["john", 75],
#     ["paul", 67],
#     ["george", 82],
#     ["ringo", 51],
# ]
# lowest = float("inf")
# name = ""
# for record in records:
#     if record[1] < lowest:
#         lowest = record[1]
#         name = record[0]
#
# lowest = float("inf")
# for record in records:
#     if record[1] == lowest:
#         continue
#     if record[1] < lowest:
#         lowest = record[1]
#         name = record[0]
# print(name, lowest, "done") #looking for: [paul, 67]


records = [
    ["john", 10075],
    ["paul", 10067],
    ["george", 10082],
    ["ringo", 10051],
]
lowest = float("inf")
name = ""
for record in records:
    if record[1] < lowest:
        lowest = record[1]
        name = record[0]
actual_lowest = lowest
lowest = float("inf")
for record in records:
    if record[1] == actual_lowest:
        continue
    if record[1] < lowest:
        lowest = record[1]
        name = record[0]
print(name, lowest)


