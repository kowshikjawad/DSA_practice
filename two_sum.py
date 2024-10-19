from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            #print(diff)
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print(prevMap[n])

solution = Solution()

# Define the input parameters
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum method and print the result
result = solution.twoSum(nums, target)
print(result)
