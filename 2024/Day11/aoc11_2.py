import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input11.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    nums = f.read().split()
    nums = [int(num) for num in nums]

print(nums)

DP = [defaultdict(lambda: 1) if i == 0 else defaultdict(lambda: -1) for i in range(76)]

def solve(nr, no_blinks):
    if DP[no_blinks][nr] != -1:
        return DP[no_blinks][nr]
    
    if nr == 0:
        DP[no_blinks][nr] = solve(1, no_blinks-1)
    elif len(str(nr)) % 2 == 0:
        ln = len(str(nr))
        v1 = int(nr//(10**(ln/2)))
        v2 = int(nr%(10**(ln/2)))

        DP[no_blinks][nr] = solve(v1, no_blinks-1) + solve(v2, no_blinks-1)
    else:
        DP[no_blinks][nr] = solve(nr*2024, no_blinks-1)

    return DP[no_blinks][nr]

total = 0
for num in nums:
    total += solve(num, 75)

print(total)