from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # add each element to hashMap as a key with the index as value
        hashMap = {}
        # iterate over nums
        for i in range(len(nums)):
            # if target minus num is in hashMap
            complement = target - nums[i]
            if  complement in hashMap and i != hashMap[complement]: 
                # return i and hashMap value at target minus num
                return [i, hashMap[complement]]