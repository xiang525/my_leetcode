"""
jiuzhang solution
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:return None
        if root is p or root is q:#找到第一个点就return了， 这是关键
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:return root
        if left:return left
        if right:return right
        return None
        