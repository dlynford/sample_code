# 2/3/2022


# Hacker rank url: https://www.hackerrank.com/challenges/python-division/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // .
# The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

#input
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))

division = a / b
floor_division = a//b

# output:
print(floor_division)
print(division)

