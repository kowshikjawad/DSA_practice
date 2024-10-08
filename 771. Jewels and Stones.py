from itertools import count
import collections
jewels = "aA" 
stones = "aAAbbbb"

count = 0

s_list = list(stones)
j_list = list(jewels)

for i in jewels:
    for j in stones:
        if i == j:
            count += 1
print(s_list.count('A'))