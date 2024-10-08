from itertools import count
import collections


nums = [1,2,3,1,1,3]
h = collections.Counter(nums)

print(h)

for val in h.values():
    print(val)


    
    