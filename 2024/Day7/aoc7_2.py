import os

script_dir = os.path.dirname(__file__)
rel_path = "input7.txt"
abs_file_path = os.path.join(script_dir, rel_path)

sol = 0

def poss(target, curr, i):
    if i == len(nums):
        return target == curr

    return poss(target, curr * nums[i], i+1) or poss(target, curr + nums[i], i+1) or poss(target, int(str(curr) + str(nums[i])), i+1)

with open(abs_file_path) as f:
    for line in f:
        lines = line.split(':')
        target = int(lines[0])
        nums = [int(el) for el in lines[1].split()]

        if poss(target, nums[0], 1):
            sol += target

print(sol)