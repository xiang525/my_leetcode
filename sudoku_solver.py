"""
# 数独的目标是以数字填充一个9×9网格，而使每行，每列和每个宫（即3×3的大格）包含所有1至9的数字。
# 解题思路：使用dfs来解决问题。
# similar to valid sudoku
"""
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def check(self,x,y,board): # check的同时也赋值
    	tmp = board[x][y]
    	board[x][y] == '.'
    	for row in range(9):
    		if board[row][y] == tmp:
    			return False
    	for col in range(9):
    		if board[x][col] == tmp:
    			return False
    	for row in range(3):
    		for col in range(3):
    			if board[(x/3)*3+row][(y/3)*3+col] == tmp:
    				return False
    	board[x][y] = tmp
    	return True

    def dfs(self,board):
    	for row in range(9):
    		for col in range(9):
    			if board[row][col] == '.':
    				for char in '123456789':
    					board[row][col] = char
    					if self.check(row,col,board) and self.dfs(board): #当check is true, 加入新char后board变了，所以要递归dfs(board), 
    						return True
    					else:
    						board[row][col] = '.'
    				return False
    	return True



    def solveSudoku(self, board):
    	self.dfs(board)  #因为不能return任何值，所以写成dfs可以避免return






class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def check(self, x, y, board):  
        tmp = board[x][y]  
        board[x][y] = '.'  
        for row in range(9):  
            if board[row][y] == tmp:  
                return False  
        for col in range(9):  
            if board[x][col] == tmp:  
                return False  
        for row in range(3):  
            for col in range(3):  
                if board[(x / 3) * 3 + row][(y / 3) * 3 + col] == tmp:  
                    return False  
        board[x][y] = tmp  
        return True 

    def dfs(self, board):  
        for row in range(9):  
            for col in range(9):  
                if board[row][col] == '.':  
                    for char in '123456789':  
                        board[row][col] = char  
                        if self.check(row, col, board) and self.dfs(board):  
                            return True  
                        else:board[row][col] = '.'  
                    return False  
        return True  
    def solveSudoku(self, board):  
        self.dfs(board) 


