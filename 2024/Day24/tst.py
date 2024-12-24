import os

script_dir = os.path.dirname(__file__)
rel_path = "input24.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path)

# Parse the input
for line in file:
    if line.isspace():
        break  # End of wire values section

formulas = {}

# Parse gate formulas
for line in file:
    x, op, y, z = line.replace(" -> ", " ").split()
    formulas[z] = (op, x, y)

# Utility function to format wire names
def make_wire(char, num):
    return char + str(num).rjust(2, "0")

# Recursive verification functions
def verify_z(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

def verify_intermediate_xor(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return (verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)) or \
           (verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1))

def verify_direct_carry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

# Verify a specific wire number
def verify(num):
    return verify_z(make_wire("z", num), num)

# Calculate how far the system progresses
def progress():
    i = 0
    while True:
        if not verify(i):
            break
        i += 1
    return i

# Identify swapped wires
swaps = []

for _ in range(4):  # There are 4 pairs of swapped wires
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y:
                continue
            # Swap the formulas for x and y
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:  # Check if the swap improves progress
                break
            # Restore the original formulas if the swap is not beneficial
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]  # Add the swapped pair to the list

print(",".join(sorted(swaps)))
