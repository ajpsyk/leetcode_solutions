from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # intialize start, end, middle of binary search
        start = 0
        end = len(matrix) - 1
        target_row = []
        # binary search over matrix until start and end overlap
        while start <= end:
            middle = start + (end - start) // 2
            print(target, matrix[middle][0], matrix[middle][-1])
            # if middle is within row
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                # we found the row
                # update start and end
                target_row = matrix[middle]
                start = end + 1
            # else target is less than start of row
            elif target < matrix[middle][0]:
                # update end to be middle - 1
                end = middle - 1
            # else target is greater than end of row
            else:
                # update start to be middle + 1
                start = middle + 1
        # do binary search on middle
        row_start = 0
        row_end = len(target_row) - 1

        while row_start < row_end:
            row_middle = row_start + (row_end - row_start) // 2

            if target == target_row[row_middle]:
                return True
            elif target < target_row[row_middle]:
                row_end = row_middle - 1
            else:
                row_start = row_middle + 1
        
        return False