from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize largest_container at zero
        largest_container = 0
        # initialize left pointer at 0
        left = 0
        # initialize right pointer at len(height) - 1
        right = len(height) - 1
        # iterate until left and right are at same index
        while left < right:
            # store index distance * height of the shorter number
            height_left = height[left]
            height_right = height[right]
            area = min(height_left, height_right) * (right - left)
            largest_container = max(largest_container, area) 
            # if left is smaller than right
            if height_left < height_right:
                # increment left
                left += 1
            # else
            else:
                # decrement right
                right -= 1
        # return largest_container
        return largest_container