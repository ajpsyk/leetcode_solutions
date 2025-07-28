from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # intialize start, end,
        m = len(matrix)
        n = len(matrix[0])
        # flatten matrix
        start = 0
        end = m * n - 1
        # binary search over flattend matrix
        while start <= end:
            middle = start + (end - start) // 2
            # map coordinates back to 2d matrix
            value = matrix[middle // n][middle % n]
            if target == value:
                return True
            elif target < value:
                end = middle - 1
            else:
                start = middle + 1
        return False