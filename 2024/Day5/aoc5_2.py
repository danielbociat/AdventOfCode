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
            
            if not correct:
                correct_nums = list()
                assigned = list()
                nums_set = set(nums)
                for i in range(len(nums)):
                    mini = list(nums_set.difference(assigned))[0]
                    for el2 in nums_set.difference(assigned):
                        if mini in dependencies[el2]:
                            mini = el2

                    #print(mini)
                    assigned.append(mini)

                # print(assigned)
                total += assigned[len(assigned)//2]

print(total)