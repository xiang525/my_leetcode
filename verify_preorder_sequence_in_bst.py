"""
不是最优解 O(n) complexity and O(n) space
"""
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        lower = -sys.maxint
        for e in preorder:
            if e < lower:
                return False
            while stack and e > stack[-1]:
                lower = stack.pop()
            stack.append(e)
        return True
                

"""
O(n) complexity and O(1) space
直接利用preorder不用新开空间, 但是要改变指针 i 
"""

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
       
        lower = -sys.maxint
        i = 0
        for e in preorder:
            if e < lower:
                return False
            while i > 0 and e > preorder[i-1]:
                lower = preorder[i-1]
                i -= 1
            preorder[i] = e
            i += 1
        return True



