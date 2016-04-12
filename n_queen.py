class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i] == j or abs(k - i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1, valuelist + [s[:i] + 'Q' + s[i + 1:]])
        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res


"""
论坛里的版本
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        

# nums is a one-dimension array, like [1, 3, 0, 2] means
# first queen is placed in column 1, second queen is placed
# in column 3, etc.
        def dfs(nums, depth, value):
            if depth == len(nums):
                res.append(value)
                return  # backtracking
            for i in xrange(len(nums)):
                nums[depth] = i
                if self.valid(nums, depth):  # pruning
                    tmp = "."*len(nums)
                    dfs(nums, depth+1, value+[tmp[:i]+"Q"+tmp[i+1:]])
        res = []
        dfs([-1]*n, 0, [])
        return res

# check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in xrange(n):
            if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n] :
                return False
        return True











































