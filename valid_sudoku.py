class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:return False
            for i in range(9):
                if board[x][i]==tmp:return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: # this will make replicate checks
                    	return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                	continue
                tmp=board[i][j]
                board[i][j]='D'  # why do we need this?
                if isValid(i,j,tmp)==False: 
                	return False
                else:
                    board[i][j]=tmp
        return True





"""
# 验证已经填好的数独是否合符规则。
# 思路：
# 行，列和小九宫分别检查就可以了。
# 有填好数字的就检查，没填写的可以不管。
# 但是也可以一起同时检查，时间效率稍微快一点，不过需要额外空间。
"""





























