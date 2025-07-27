from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialize stack
        stack = []
        # initialize max area
        max_area = 0
        # iterate over index and value of heights
        for index, height in enumerate(heights):
            # while height is less than top of stack height
            curr_index = index
            while stack and height < stack[-1][1]:
                # pop the top of stack
                pop = stack.pop()
                # multiply pop height by difference of current index and index stored in height of stack to get area
                # compare area with max area and update if greater
                max_area = max(max_area, pop[1] * (index - pop[0]))
                # add left index boundary and height to the stack
                # update left boundary of current height to the smaller popped height
                curr_index = pop[0]
            stack.append((curr_index, height))
        # if there is stuff remaining in the stack, iterate over stack and update max area
        for index, height in stack:
            max_area = max(max_area, height * (len(height) - index))
        return max_area