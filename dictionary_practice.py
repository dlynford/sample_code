# 1/30/2022
dict = {}
dict['rolls_per_game'] = 10
dict['games'] = 5
dict['players'] = 5

# output:
# {'rolls_per_game': 10, 'games': 5, 'players': 5}

sum_values = dict.values()
# print(sum_values)

# output:
# dict_values([10, 5, 5])


# for keys, values in dict.items():
# number_list = [7, 2, 8, 2, 10, 7, 1, 8, 2, 7, 3, 10, 10, 5, 4, 8, 2, 7]
#
# for number in number_list:
#     print(number)
#
# print(sum(number_list))
# print(len(number_list))

def repeat(string, n):
    for i in range(n):
        print(string, end="")


# repeat("why?", 5)
# why?why?why?why?why?

# repeat("nine",3)
# nineninenine


# def stringing(string, n):
#     result = ""
#     for i in range(1, n+1):
#         result = result + string
#         print(result)


# stringing("nope", 7)
# # output:
# # nope
# # nopenope
# # nopenopenope
# # nopenopenopenope
# # nopenopenopenopenope
# # nopenopenopenopenopenope
# # nopenopenopenopenopenopenope

for i in range(len("no_need")):
    print(i, end=" ")
# output:
# 0 1 2 3 4 5 6

