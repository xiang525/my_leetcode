class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board); n = len(board[0])
        dx = (1,-1,0,0,1,-1,-1,1)
        dy = (1,-1,1,-1,0,0,1,-1)
        for x in range(m):
            for y in range(n):
                value = 0
                for k in range(8):
                    i = x + dx[k]
                    j = y + dy[k]
                    value += self.status(board,i,j)
                if value == 3 or value + board[x][y] == 3:
                    board[x][y] |= 2
                    
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

                
    def status(self,board,i,j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return 0
        print board[i][j], board[i][j] & 1
        return board[i][j] & 1
      
        


if __name__ == "__main__":
    Solution().gameOfLife([[1,1],[1,0]])












