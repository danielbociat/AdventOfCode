arr1 = list()
arr2 = list()

with open("input1.txt") as f:
    for line in f:
        nums = line.split()
        arr1.append(int(nums[0]))
        arr2.append(int(nums[1]))

arr1 = sorted(arr1)
arr2 = sorted(arr2)

diff = 0
for i in range(len(arr1)):
    diff += abs(arr1[i] - arr2[i])

print(diff)
