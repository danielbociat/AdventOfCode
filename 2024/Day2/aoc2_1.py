total = 0

with open("input2.txt") as f:
    for line in f:
        nums = [int(c) for c in line.split()]
        is_safe = True

        is_inc = True
        if nums[1] < nums[0]:
            is_inc = False

        for i in range(1, len(nums)):
            dif = abs(nums[i] - nums[i-1]) 
            if dif < 1 or dif > 3:
                is_safe = False
                break

            if (is_inc and nums[i] < nums[i-1]) or (not is_inc and nums[i] > nums[i-1]):
                is_safe = False
                break
        
        if is_safe:
            total += 1

print(total)