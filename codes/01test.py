'''
594. Longest Harmonious Subsequence
'''
from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_length = 0
        
        print(counter)
        
        for num in counter:
            if num + 1 in counter:
                print(counter[num])
                max_length = max(max_length, counter[num] + counter[num + 1])

        return max_length


sol = Solution()
# nums = [1,3,2,2,5,2,3,7]
nums = [1,2,3,4]
result = sol.findLHS(nums)
print(result)