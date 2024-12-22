import os

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

def compute_secret(num, n):

    for _ in range(n):
        num = mix(num, num * 64)
        num = prune(num)
        num = mix(num, num // 32)
        num = prune(num)
        num = mix(num, num*2048)
        num = prune(num)

    return num

total = 0
for num in mp:
    total += compute_secret(num, 2000)

print(total)