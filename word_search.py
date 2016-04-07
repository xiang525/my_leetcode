"""
# 使用DFS, 不要再开一个新的棋盘或其他很大的变量来记录状态，不然容易超时。
# 使用dfs来搜索，为了避免已经用到的字母被重复搜索，将已经用到的字母临时替换为'#'就可以了
# 多练习几遍
"""

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        self.totalRow, self.totalCol = len(board),len(board[0])
        for i in xrange(self.totalRow):
            for j in xrange(self.totalCol):
                if board[i][j] == word[0]: # 首先要找到第一个开始的点
                    if self.dfs(board,i,j,word[1:]): return True
        return False

    def dfs(self,board,r,c,word):
        if len(word) == 0 : return True
        # Up
        if (r > 0 and board[r-1][c] == word[0]):
            ch, board[r][c] = board[r][c],'#'  # 临时替换为#
            if self.dfs(board,r-1,c,word[1:]): return True
            board[r][c] = ch

        # Down
        if (r < self.totalRow-1 and board[r+1][c]==word[0]):
            ch,board[r][c] = board[r][c],'#'
            if self.dfs(board,r+1,c,word[1:]): return True
            board[r][c] = ch

        # left
        if (c > 0 and board[r][c-1]==word[0]):
            ch, board[r][c] = board[r][c],'#'
            if self.dfs(board,r,c-1,word[1:]): return True
            board[r][c] = ch

        # right
        if (c < self.totalCol-1 and board[r][c+1] == word[0]):
            ch, board[r][c] = board[r][c],'#'
            if self.dfs(board,r,c+1,word[1:]): return True
            board[r][c] = ch
        return False





















    		


