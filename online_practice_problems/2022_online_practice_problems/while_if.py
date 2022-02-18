# 2/2/2022

# i = 0
# a = "Hi Aeendreeeeewe"
# while (i < len(a)):
#     if a[i] == "e":
#         i+=1
#         continue
#     #print(i)
#     print(i, "->", a[i])
#     i += 1
#
# integer = 0
# string = "Good Morning."
# print(len(string))
# output: 13
#
# while integer < len(string):
#     # if string[integer] == "o":
#     #     integer += 1
#     #     continue
#
#     if string[integer] == "m".upper():
#         print(integer, "no need")
#         integer += 1
#
#     elif string[integer] ==" ":
#         print(integer, "long shanks")
#         integer += 1
#
#     else:
#         print(integer, "-->", string[integer])
#         integer += 1
# print("\nDone.")
#

# 2/7/2022
# i = 0
# string = "Today is Monday."
# while i < len(string):
#     if string[i] == "a":
#         i += 1
#         print(i, "^^", '$')
#
#     elif string[i] == " ":
#         print("space")
#         i +=1
#     else:
#         print(i, "^^", string[i])
#         i += 1
#
# i = 0
# s = "Let's get some lunch this afternoon."
# while i < len(s):
#     if s[i] == "s":
#         print(i, " no need")
#         i += 1
#     elif s[i] == " ":
#         print("--")
#         i += 1
#     else:
#         print(i, s[i])
#         i += 1
# print("\ndone.")


i = 0
x = "What is today's date? I forgot."
vowels = ["a", "e", "i", "o","u", "y"]
print(f"\nNumber of letters: {len(x)}")
while i < len(x):
    if x[i] in vowels:
        print(i, "vowel")
        i += 1
    elif x[i] == "s":
        print(i, x[i].upper())
        i += 1
    else:
        print(i, x[i])
        i +=1

# output:
#
# Number of letters: 31
# 0 W
# 1 h
# 2 vowel
# 3 t
# 4
# 5 vowel
# 6 S
# 7
# 8 t
# 9 vowel
# 10 d
# 11 vowel
# 12 vowel
# 13 '
# 14 S
# 15
# 16 d
# 17 vowel
# 18 t
# 19 vowel
# 20 ?
# 21
# 22 I
# 23
# 24 f
# 25 vowel
# 26 r
# 27 g
# 28 vowel
# 29 t
# 30 .





