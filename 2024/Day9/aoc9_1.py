import os

script_dir = os.path.dirname(__file__)
rel_path = "input9.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    line = f.read().splitlines()[0]

is_free = False
id = 0
mem = list()
for char in line:
    num = int(char)

    if(is_free):
        for i in range(num):
            mem.append('.')
    else:
        for i in range(num):
            mem.append(id)
        id+=1

    is_free = not is_free

left = 0
right = len(mem) - 1
while left < right:
    while mem[left] != '.':
        left+=1
    while mem[right] == '.':
        right-=1
    
    if left < right:
        mem[left], mem[right] = mem[right], mem[left]

sol = 0
curr_block = 0

for i in range(len(mem)):
    if mem[i] == '.':
        break

    sol += mem[i] * i


print(sol)