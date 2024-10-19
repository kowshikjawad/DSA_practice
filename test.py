nums = [2, 7, 11, 15]
target = 9
map = {}

for i, n in enumerate(nums):
    diff = target - nums[i]

    map[n] = i 

    if diff in nums:
        print(ma)


