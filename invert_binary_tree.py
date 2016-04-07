# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Solution 递归
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
    	if not root:
    		return None
    	tmp = TreeNode(0) # must first generate a tree structure
    	tmp = root.left
    	root.left = self.invertTree(root.right)
    	root.right = self.invertTree(tmp)
    	
    	return root
