"""递归
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
    	if not root:
    		return False
    	if root.val == sum and not root.left and not root.right:  # to the leves (forgot about this the first time)
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


"""
另一种写法
"""

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if root.val == sum and not root.left and not root.right:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
