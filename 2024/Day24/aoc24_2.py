import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input24.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read()

mp = mp.split("\n\n")

vals = defaultdict(lambda: -1)
equations = dict()

xs = list()
ys = list()

for init in mp[0].split('\n'):
    var_val = init.split(':')

    vals[var_val[0]] = int(var_val[1])

    if var_val[0][0] == 'x':
        xs.append(var_val[0])
    else:
        ys.append(var_val[0])

print(vals)

zs = list()

for eq in mp[1].split('\n'):
    eq_vars = eq.split(' ')

    equations[eq_vars[-1]] = (eq_vars[0], eq_vars[1], eq_vars[2])
    print(equations[eq_vars[-1]])    

    if eq_vars[-1][0] == 'z':
        zs.append(eq_vars[-1])

result = ""

zs = sorted(zs)
print(zs)

def get_val(key) -> int:
    if vals[key] != -1:
        return vals[key]
    
    result = -1

    var1,op,var2 = equations[key]

    if op == "AND":
        result = get_val(var1) & get_val(var2)
    if op == "OR":
        result = get_val(var1) | get_val(var2)
    if op == "XOR":
        result = get_val(var1) ^ get_val(var2)

    vals[key] = result
    return result

xVal = ''
for x in xs:
    xVal = str(get_val(x)) + xVal

print(xVal)

yVal = ''
for y in ys:
    yVal = str(get_val(y)) + yVal

print(yVal)

target = int(xVal, 2) + int(yVal, 2)
print(target)
print(bin(target)[2:])

for z in zs:
    result = str(get_val(z)) + result

print(result)
print(int(result, 2))