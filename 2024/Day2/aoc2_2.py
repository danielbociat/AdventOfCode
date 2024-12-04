import os

total = 0

def check_safe(nums):
    is_safe = True

    is_inc = True
    if nums[1] < nums[0]:
        is_inc = False
    
    for i in range(1, len(nums)):
        dif = abs(nums[i] - nums[i-1]) 
        if dif < 1 or dif > 3:
            is_safe = False
            break

        if (is_inc and nums[i] < nums[i-1]) or (not is_inc and nums[i] > nums[i-1]):
            is_safe = False
            break

    return is_safe
        

script_dir = os.path.dirname(__file__)
rel_path = "input2.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    for line in f:
        nums = [int(c) for c in line.split()]
        
        if check_safe(nums):
            total += 1
        else:
            for i in range(len(nums)):
                if check_safe(nums[:i] + nums[i+1:]):
                    total += 1
                    break

print(total)