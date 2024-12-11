import os

script_dir = os.path.dirname(__file__)
rel_path = "input11.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    nums = f.read().split()
    nums = [int(num) for num in nums]

print(nums)

for i in range(25):
    new_list = list()
    for num in nums:
        if num == 0:
            new_list.append(1)
        elif len(str(num)) % 2 == 0:
            ln = len(str(num))
            v1 = int(num//(10**(ln/2)))
            v2 = int(num % 10**(ln/2))

            new_list.append(v1)
            new_list.append(v2)

        else:
            new_list.append(num * 2024)

    nums = new_list

print(len(nums))