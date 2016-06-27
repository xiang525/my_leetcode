# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
这是一种分治的思想
"""
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
    	
    	if not root:
    		return 0
    	return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# the same as balanced tree


"""
九章给的答案: divide conquer
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left) 
        right = self.maxDepth(root.right) 
        return max(left,right) + 1


"""
非递归解法， 和level order 题一样的思想
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                pop = queue.pop(0)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            level += 1
        return level



