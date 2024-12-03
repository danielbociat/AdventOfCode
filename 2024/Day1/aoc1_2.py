from collections import defaultdict

arr1 = list()
arr2 = list()

mp = defaultdict(lambda: 0)

with open("input1.txt") as f:
    for line in f:
        nums = line.split()
        arr1.append(int(nums[0]))
        
        mp[int(nums[1])] += 1

similarity = 0

# print(arr1)
# print(mp)

for el in arr1:
    similarity = similarity + el * mp[el]


print(similarity)
