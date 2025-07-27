from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create stack of index and values
        stack = []
        # create output * len temps
        output = [0] * len(temperatures)
        # iterate through temperature indexes and values
        for index, value in enumerate(temperatures):
            # while stack and temps val is greater than peek at val
            while stack and value > stack[len(stack) - 1][1]:
                # save stack.pop()
                pop = stack.pop()
                # output at stack.pop() index = i - stack.pop() index
                output[pop[0]] = index - pop[0]
            # push i and temp tuple to stack
            stack.append((index, value))
        return output