import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input19.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    lines = f.read().splitlines()

patterns = lines[0].split(", ")
print(patterns)

DP = defaultdict(lambda: -1)
DP[""] = 1

def minus(word, suffix):
    if len(suffix) > len(word):
        return ""
    
    n = len(suffix) - 1
    m = len(word) - 1

    while n >= 0 and suffix[n] == word[m]:
        n -= 1
        m -= 1

    if(n != -1): 
        return ""
    
    return word[:m+1]

def solve(word):
    if DP[word] != -1:
        return DP[word]
    
    solvable = 0
    for pattern in patterns:
        s = minus(word, pattern) 

        if s != "":
            solvable = solvable + solve(s)

    DP[word] = solvable
    return DP[word]

patterns = sorted(patterns, key = lambda x : len(x))

for pattern in patterns:
    solve(pattern)

    DP[pattern] += 1

total = 0 
for word in lines[2:]:
    solve(word)
    if DP[word] >= 1:
        # print("A", word)
        total += DP[word]

print(total)