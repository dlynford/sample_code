# 2/3/2022
# Sample Test question 1 Hacker Rank
#Learn how to iterate through strings.

string = "a blue moon"

def transformSentence(string):
    phrase = []
    for index, letter in enumerate(string):
        # print(letter, end="_")
        if index > 0:
            if string[index] > string[index-1]:
                letter = string[index].upper()
            elif string[index] < string[index-1]:
                letter = string[index].lower()
        phrase.append(letter)
    return ''.join(phrase)


# print(transformSentence(string))
#
# numbers = list(range(1, 1001))
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#     elif number % 2 != 0:
#         print("$")





# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# 1, 102, 3, 104, 5, 106, 7, 108, 9, 110, 11, 112, 13, 114, 15, 116, 17, 118, 19, 120, 21, 122, 23, 124, 25,

# phrase = "If not now then when."
# vowels = ["a", "e", "i", "o", "u", "y"]
#
# for index, letter in enumerate(phrase):
#     if letter in vowels:
#         print("*", end="")
#     else:
#         print(letter, end="")

# output:
# If n*t n*w th*n wh*n.


phrase = "If not now then when."
vowels = ["a", "e", "i", "o", "u", "y"]
characters =["#", "@", "$", "%", "&", "*"]
#
# for index, letter in enumerate(phrase):
#     if phrase[index] == 2:
#         for character in characters:
#             print(character)

#
# fav_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c', "Java", "javascript", "perl"],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# Show all responses for each person.
# for name, langs in fav_languages.items():
#     print(f"{name}: ")
#     for lang in langs:
#         print(f"- {lang}")
# for key, values in fav_languages.items():
#     print(f"{key.title()} knows the following languages: ")
#     for value in values:
#         print(f"\t{value}")

# nums = list(range(0, 15))
# print(nums)
#
# for num in nums:
#     if 4 <= num < 11:
#         print(num, "abc", end="")
#     else:
#         print(num, end=" ")

# output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# 0 1 2 3 4 abc5 abc6 abc7 abc8 abc9 abc10 abc11 12 13 14
