import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input25.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    schemas = f.read()

schemas = schemas.split("\n\n")

locks = list()
keys = list()

for schema in schemas:
    schema = schema.split('\n')

    if schema[0] == '#####':
        print("lock")
        lock = []
        for j in range(5):
            depth = 0
            for i in range(1,7):
                if schema[i][j] == '#':
                    depth+=1
                else:
                    break

            lock.append(depth)
        
        locks.append(lock.copy())


    if schema[-1] == '#####':
        print("key")

        key = []
        for j in range(5):
            depth = 0
            for i in range(0,6):
                if schema[i][j] == '.':
                    depth+=1
                else:
                    break

            key.append(6 - depth)
        
        keys.append(key.copy())


print(schemas)
print(locks)
print(keys)

total = 0

for key in keys:
    for lock in locks:
        flag = True

        for i in range(5):
            if key[i] + lock[i] >= 6:
                flag = False
                break

        if flag:
            total += 1

print(total)