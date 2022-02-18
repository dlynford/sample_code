# 2/17/2022
# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True,
# in which case return True if the number is less or equal to 1, or greater or equal to 10.
#
#
# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True


def one_to_ten(n, outside_mode):
    if outside_mode:
        return True
    if 1 <= n <= 10:
        return True

    # if n >=1 and n <=10:
    #     return True
    else:
        return False

print(one_to_ten(9, True))