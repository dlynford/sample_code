# 2/2/2022
# I am interested to learn how to create lists the length of strings, and manipulate those lists.

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
ask = input("What city/town were you born in? ")
length = len(ask)

# print(length)
for i in range(length):
    if ask[i] in vowels:
        output = ask
print(output)


# sample code from: text_to_morse_code.py
# ask = input("type: ")
# length = len(ask)
# output = ""
# for i in range(length):
#     if ask[i] in symbols.keys():
#         output = output + " " + symbols.get(ask[i])
#
# print(output)

