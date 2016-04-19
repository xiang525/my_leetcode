"""
O(m+n):有个规律凡是左边上面的都小于当前值， 右边下面的都大于当前值
此题没有O(logmn)的解法， 有点难用binary search，不是不可以
(1) Start at the bottom-left corner.
(2) If the target is less than that value, it must be above us, so move up one.
(3) Otherwise we know that the target can't be in that column, so move right one.
(4) Goto 2.
stack overflow有好的解释可以看看
http://stackoverflow.com/questions/2457792/given-a-2d-array-sorted-in-increasing-order-from-left-to-right-and-top-to-bottom/2458113#2458113
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix); m = len(matrix[0])
        # from bottom left to top right
        x = n - 1; y = 0
        while x >= 0 and y < m:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                return True
        return False