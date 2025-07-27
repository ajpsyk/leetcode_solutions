from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort input by position
        pair = sorted(zip(position, speed))
        stack = []
        # iterate over pairs, furthest distance car first
        for p, s in reversed(pair):
            # push to stack
            stack.append((target - p) / s)
            # compare top 2 cars in stack
            # if top car finishes in less time, pop it because its in the fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)