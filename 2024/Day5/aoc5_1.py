import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input5.txt"
abs_file_path = os.path.join(script_dir, rel_path)


dependencies = defaultdict(lambda: set())
search_depencies = True

total = 0

with open(abs_file_path) as f:
    for line in f:
        if search_depencies:
            dependency = line.split('|')

            if len(dependency) != 2:
                search_depencies = False
            else:
                dependencies[int(dependency[0])].add(int(dependency[1]))

        else:
            nums = [int(el) for el in line.split(',')]
            viewed = set()

            correct = True
            for num in nums:
                # print(num, dependencies[num])
                # print(viewed)
                for el in dependencies[num]:
                    if el in viewed:
                        
                        correct = False
                        break
                
                if correct:
                    viewed.add(num)
                else:
                    break
            
            if correct:
                total += nums[len(nums)//2]

print(total)