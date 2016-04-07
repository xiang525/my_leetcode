
"""
jiuzhang 模板 binary search O(logn)
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0; right = n
        while left+1 < right:
            m = (left+right)/2
            if isBadVersion(m):
                right = m
            else:
                left = m
        if isBadVersion(left):
            return left
        return right
        