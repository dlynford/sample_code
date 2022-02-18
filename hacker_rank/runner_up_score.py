# 2/7/2022

# n = int(input())
# arr = map(int, input().split())

def add(n):
    addition = n + n
    return addition


def adder(n):
    addition = n + n
    print(addition)

numbers = [1,2,3]
nums = [3,4,5]
map_func = map(add, numbers)
print(list(map_func))

adder(nums)