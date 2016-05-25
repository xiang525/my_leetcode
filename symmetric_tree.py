# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
    	if not root:
    		return True
    	return self.isSymmetricTree(root.left,root.right)

    def isSymmetricTree(self,node1,node2):
    	if node1 and node2:
    		return node1.val == node2.val and self.isSymmetricTree(node1.left,node2.right) and self.isSymmetricTree(node1.right,node2.left)
    	else:
    		return node1 == node2

"""递归
"""


"""
另一种写法
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node1,node2):
            if node1 and node2:
                return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
            return node1 == node2
        
        if not root: return True
        return helper(root.left, root.right)




