"""
https://leetcode.com/problems/valid-sudoku/
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
class Solution(object):
    def isValidSudoku(self, board):
        return  self.is9by9Valid(board) and self.isRowValid(board) and self.isColValid(board)
    
    def isRowValid(self, board):
        for row in board:
            nums = {}
            for cell in row:
                if(not self.isCellValid(cell, nums)):
                    return False
        return True
    
    def isCellValid(self, cell, nums):
        if(cell != "."):
            if(cell not in nums):
                nums[cell] = 1
                return True
            else:
                return False
        else:
            return True
    def isColValid(self, board):
        col = 0
        while(col < 9):
            row = 0
            nums = {}
            while(row < 9):
                if(not self.isCellValid(board[row][col], nums)):
                    return False
                row += 1
            col += 1
        return True
    
    def is9by9Valid(self, board):
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if(not self.is3by3Valid(board, row, col)):
                    return False
        return True
    
    def is3by3Valid(self, board, rowStartIdx, colStartIdx):
        row = rowStartIdx
        nums = {}
        while(row < rowStartIdx+3):
            col = colStartIdx
            while(col < colStartIdx+3):
                if(not self.isCellValid(board[row][col], nums)):
                    return False
                col += 1
            row += 1
        return True
                