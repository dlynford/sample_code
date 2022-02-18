# 2/12/2022

scores = [75, 66, 83, 92, 17, 49, 56, 76, 80]
number_of_scores = len(scores)
print(f"Number of scores = {number_of_scores}")


lowest = 101
message = "Lowest score"
for score in scores:
    if score < lowest:
        lowest = score
print(f"{message}: {lowest}")
low_score = lowest

lowest = 101
for score in scores:
    if score == low_score:
        continue
    if score < lowest:
        lowest = score
print(f"Second lowest score: {lowest}")
