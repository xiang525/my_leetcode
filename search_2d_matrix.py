"""
O(m+n) not the best solution，even if it is already good.
分析一下这种矩阵的特点（九章讲得很好),从下往上看，头元素是这一行最小的， 这一列
最大的，根据这个特点移动。 从右上角开始。
"""
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        j = len(matrix[0])-1;i=0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

"""
和上面一样的思路但是从左下角开始，写法上有点不同 O(m+n)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:return False
        m = len(matrix);n = len(matrix[0])
        j = 0; i = m-1
        while j < n and i >= 0:
            if matrix[i][j] == target:return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


"""
九章模板 O(logm + logn)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
        
        
            
            
            
            
            
        
























