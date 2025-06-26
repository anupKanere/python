from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for index , num in enumerate(nums):
            compliment = target - num
            if compliment in num_index:
                return [num_index[compliment] , index]
            num_index[num] = index
        return []
    
    def twoSumValidation(self , nums : List[int] , target : int) -> List[int]:
        if len(nums) < 2:
            return []
        num_maps = {}

        for i , val in enumerate(nums):
            compliment = target - val
            if compliment in num_maps:
                return [num_maps[compliment] , i]
            num_maps[val] = i
        return []
    
    def two_sum_sorted(self , nums : List[int] , target : int) -> int:

        if len(nums) < 2:
            return []

        pairs = [(num , index) for index , num in enumerate(nums)]
        pairs.sort()
        left , right = 0 , len(pairs) - 1

        while left < right:
            curr_sum = pairs[left][0] + pairs[right][0]
            if curr_sum == target:
                return [pairs[left][1] , pairs[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []

if __name__ == "__main__":
    sol = Solution()

    nums = [2,7,11, 8 ,15]
    target = 9

    # nums = [3,2,4]
    # target = 6

    two_sum_1 = sol.twoSum(nums , target )
    print(f"two sum :- {two_sum_1}")

    two_sum_2 = sol.twoSumValidation(nums , target )
    print(f"two sum validation :- {two_sum_2}")

    two_sum_3 = sol.two_sum_sorted(nums , target )
    print(f"two sum Sorted :- {two_sum_3}")
