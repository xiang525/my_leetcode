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
论坛里简洁的做法
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {}
        for i in xrange(0,9):
            for j in xrange(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i/3,j/3,cur))
        return True

"""
也可以用array
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    tmp = board[i][j]
                    if (i,tmp) in d or (tmp,j) in d or (i/3,j/3,tmp) in d:
                        return False
                    d.append((i,tmp))
                    d.append((tmp,j))
                    d.append((i/3,j/3,tmp))
        return True



"""
# 验证已经填好的数独是否合符规则。
# 思路：
# 行，列和小九宫分别检查就可以了。
# 有填好数字的就检查，没填写的可以不管。
# 但是也可以一起同时检查，时间效率稍微快一点，不过需要额外空间。
"""





























