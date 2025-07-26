from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # initialize left and right pointer
        left = 0
        right = len(height) - 1
        # initlalize left and right max
        left_max = height[left]
        right_max = height[right]
        # total
        total = 0

        # increment left and right pointer until they overlap
        while left < right:
            # if left is smaller
            if left_max < right_max:
                # increment left
                left += 1
                # find max between height at left and left max
                left_max = max(left_max, height[left])
                # add difference to total
                total += left_max - height[left]
            # else
            else:
                # decrement right
                right -= 1
                # update maxRight if height at right is larger
                right_max = max(right_max, height[right])
                # add difference to total
                total += right_max - height[right]
                
        return total