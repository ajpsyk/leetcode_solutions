from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # create max of left or right
        total = 0
        max_left = []
        max_right = []
        for left in range(len(height)):
            right = len(height) - 1 - left
            if left == 0:
                max_left.append(height[left])
                max_right.append(height[right])
            else:
                max_left.append(max(max_left[left - 1], height[left - 1]))
                max_right.append(max(max_right[left - 1], height[right + 1]))
        # determine water held by subtractin current height from min on left or right
        for left in range(len(height)):
            right = len(height) - 1 - left
            total += max(min(max_left[left], max_right[right]) - height[left], 0)
        return total

solution = Solution()
solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])