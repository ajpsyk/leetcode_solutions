from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find half of total
        total = len(nums1) + len(nums2)
        half = total // 2
        # assign array to be searched to the smaller array
        if len(nums1) <= len(nums2):
            small_nums = nums1
            large_nums = nums2
        else:
            small_nums = nums2
            large_nums = nums1
        # initialize start and end of smaller array
        start = 0
        end = len(small_nums) - 1
        # while some exit condition
        while True:
            # find the middle index of  small nums
            # we determine the index of nums two by subracting middle index of nums1 + 1 from half of total
            middle_1 = start + (end - start) // 2
            middle_2 = half - middle_1 - 2
            left_1 = small_nums[middle_1] if middle_1 >= 0 else float('-inf')
            right_1 = small_nums[middle_1 + 1] if (middle_1 + 1) < len(small_nums) else float('inf')
            left_2 = large_nums[middle_2] if middle_2 >= 0 else float('-inf')
            right_2 = large_nums[middle_2 + 1] if (middle_2 + 1) < len(large_nums) else float('inf')

            # if nums1 at middle index <= nums2 at left AND nums2 at middle index <= nums1 at middle index + 1:
            if left_1 <= right_2 and left_2 <= right_1:
                # we have our partitions set
                # return max(middle_nums1, middle_nums2)
                # odd
                if total % 2:
                    return min(right_1, right_2)
                # even
                return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_2 > right_1:
                start = middle_1 + 1
            else:
                end = middle_1 - 1