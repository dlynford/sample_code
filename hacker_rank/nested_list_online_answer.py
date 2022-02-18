# 2/8/2022

records = [
    ["john", 75],
    ["paul", 67],
    ["george", 82],
    ["ringo", 51],
]
# print(records[3][1])
print(f"Unsorted scores: {records}")
sorted_records = sorted(records, reverse=True)
print(f"\nReverse sorted scores:{sorted_records}")

for record in sorted_records:
    if record == sorted_records[0]:
        del sorted_records[0]
print(sorted_records[0])



# online answer
Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1]
    for a,c in sorted(Result):
        if c==b:
            print(a)

