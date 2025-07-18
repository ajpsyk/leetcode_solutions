from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1