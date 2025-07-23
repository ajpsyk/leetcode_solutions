from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no duplicates in rows
        # iterate over board
        for row in board:
            num_count = 0
            for element in row:
                if element != '.':
                    num_count += 1
            num_set = set(row)
            num_set.discard(".")
            if num_count != len(num_set):
                return False
            # add list to set
            # check if
        # no duplicates in columns
        for j in range(len(board)):
            num_count = 0
            col = []
            for row in board:
                col.append(row[j])
                if row[j] != '.':
                    num_count += 1
            num_set = set(col)
            num_set.discard(".")
            if num_count != len(num_set):
                return False
        
        # 0,0 then 0,1 then 0,2
        # 1,0 then 1,1, then 1,2
        # 2,0, then 2,1 then 2,2
        box_count = 0
        box_nums = []
        for i in range(0,3):
            for j in range(0,3):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False
        #THEN

        # 0,4, then 0,5 then 0,6
        # 1,4, then 1,5 then 1,6
        # 2,4 then 2,5 then 2,6
        box_count = 0
        box_nums = []
        for i in range(0,3):
            for j in range(3,6):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False
        
        box_count = 0
        box_nums = []
        for i in range(0,3):
            for j in range(6,9):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False

        box_count = 0
        box_nums = []
        for i in range(3,6):
            for j in range(0,3):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False
        
        box_count = 0
        box_nums = []
        for i in range(3,6):
            for j in range(3,6):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False

        box_count = 0
        box_nums = []
        for i in range(3,6):
            for j in range(6,9):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False

        box_count = 0
        box_nums = []
        for i in range(6,9):
            for j in range(0,3):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False

        box_count = 0
        box_nums = []
        for i in range(6,9):
            for j in range(3,6):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False

        box_count = 0
        box_nums = []
        for i in range(6,9):
            for j in range(6,9):
                box_nums.append(board[i][j])
                if board[i][j] != ".":
                    box_count += 1
        set_nums = set(box_nums)
        set_nums.discard(".")
        if box_count != len(set_nums):
            return False
        return True