from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize output
        n = len(nums)
        output = [1] * n

        # multiply prefixes to output array
        # total is 1
        total = 1
        # iterate over num indexes, not including final index
        for i in range(len(nums) - 1):
            # multiply total by num at index
            total *= nums[i]
            # multiply output at index + 1 by total
            output[i + 1] *= total

        
        # multiply postfixes to output array
        # total is 1
        total = 1
        # iterate over reverse nums, not including final index
        for i in reversed(range(1, len(nums))):
            # multiply total by num at index
            total *= nums[i]
            # multiply output at index - 1 by total 
            output[i - 1] *= total
        return output
    