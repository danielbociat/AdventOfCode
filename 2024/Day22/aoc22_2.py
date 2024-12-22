import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input22.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

mp = [int(el) for el in mp]

def mix(a,b):
    return a^b

def prune(a):
    return a % 16777216

to_occ = [-2,1,-1,3]

def compute_next(num):
    num = mix(num, num * 64)
    num = prune(num)
    num = mix(num, num // 32)
    num = prune(num)
    num = mix(num, num*2048)
    num = prune(num)

    return num

total = 0
best_configs = defaultdict(lambda: 0)

for num in mp:
    l = [num]
    nxt = num

    for _ in range(2000):
        nxt = compute_next(nxt)
        l.append(nxt)

    last_digit = [el%10 for el in l]
    diffs = [j-i for i,j in zip(last_digit, last_digit[1:])]
    configs = set()

    for diff1,diff2,diff3,diff4,el in zip(diffs, diffs[1:], diffs[2:], diffs[3:], last_digit[4:]):
        if (diff1,diff2,diff3,diff4) not in configs:
            configs.add((diff1,diff2,diff3,diff4))
            best_configs[(diff1,diff2,diff3,diff4)] += el

print(max(best_configs[cfg] for cfg in best_configs))