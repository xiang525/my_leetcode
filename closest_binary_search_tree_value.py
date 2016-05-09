"""
whatsapp phone interview
O(logn), constant space
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:return sys.maxint
        if not root.left and not root.right:
            return root.val
        left = self.closestValue(root.left,target)
        right = self.closestValue(root.right,target)
        return min([root.val, left, right], key=lambda x:abs(x-target))