from collections import defaultdict
import os

arr1 = list()
arr2 = list()

mp = defaultdict(lambda: 0)

script_dir = os.path.dirname(__file__)
rel_path = "input1.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
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
