from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search on nums
        # same start and end but with different logic
        start = 0
        end = len(nums) - 1
        # initialize min
        min_num = 5000
        # while start and end dont cross over
        while start <= end:
            # middle is same
            middle = start + (end - start) // 2
            value = nums[middle]
            # if middle is less than or equal to  end, and greater than or equal to start
            if value <= nums[end] and value >= nums[start]:
                # list is sorted and our start is our min
                return min(nums[start], min_num)
            # else if middle less than start
            elif value < nums[start]:
                # save middle as a candidate
                min_num = min(value, min_num)
                # set end to middle - 1
                end = middle - 1
            # else middle is greater than end
            else:
                # set start to middle + 1
                start = middle + 1