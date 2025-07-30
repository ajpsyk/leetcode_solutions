from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2
            value = nums[middle]
            if value == target:
                return middle
            elif nums[start] <= value:
                if target < value and target >= nums[start]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if target > value and target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        return -1