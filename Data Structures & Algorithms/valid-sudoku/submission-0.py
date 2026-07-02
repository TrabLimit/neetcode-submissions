import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # make them in to integers. empty ones are just 0
        board_copy = [[0 if (item == ".") else int(item) for item in row] for row in board]
        
        # might use Numpy to make life easier
        matrix = np.array(board_copy)
        print(matrix)

        # Check row
        i = 0
        while (i < 9):
            row = matrix[i, 0:8] 
            row = row[row != 0] # filter out empty 0s
            # print(row)
            if self.hasDuplicate(row): # check duplicates
                return False
            for number in row:
                if number not in digits: # check digits are 1-9
                    return False
            
            i += 1
        
        # Check column
        j = 0
        while (j < 9):
            column = matrix[0:8, j] 
            column = column[column != 0] # filter out empty 0s
            # print(column)
            if self.hasDuplicate(column): # check duplicates
                return False
            for number in column:
                if number not in digits: # check digits are 1-9
                    return False
            
            j += 1
        
        # Check sub-boxes
        i = 0
        j = 0

        while (i <= 9):
            while (j <= 9):
                subbox = matrix[i:i+3, j:j+3]
                # print(subbox)
                # NOTE: ravel(): Specifically built to collapse an array into 1
                subbox = subbox.ravel() 
                subbox = subbox[subbox != 0] # filter out empty 0s
                # print(subbox)
                if self.hasDuplicate(subbox): # check duplicates
                    return False
                for number in subbox:
                    if number not in digits: # check digits are 1-9
                        return False
            
                j += 3
            # Reset column and move to next 3rd row
            j = 0
            i += 3
        
        return True



    # stole from the previous problem (solution made by me)
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        nums_set = set(nums) # Convert to set (it will remove duplicates)
        if (len(nums) != len(nums_set)):
            return True
        return False



        