from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find max in piles
        # set k to max in piles
        k = 0
        for pile in piles:
            if pile > k:
                k = pile

        # binary search over range of values from 1 to max in piles, until start and end cross over
        start = 1
        end = k
        while start <= end:
            guess = start + (end - start) // 2
            # if we find a valid solution, replace k if the solution is smaller
            if self.isSolution(piles, h, guess):
                k = min(guess, k)
                end = guess - 1
            else:
                start = guess + 1
        return k
    
    def isSolution(self, piles: List[int], h: int, guess: int) -> bool:
        hours = 0
        for pile in piles:
            hours += ceil(pile / guess)
            if hours > h:
                return False
        return True