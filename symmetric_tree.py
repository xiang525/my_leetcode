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

"""
递归
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



"""
非递归写法 用stack
"""
def isSymmetric(self, root):
      if root is None:
          return True
      stack = [(root.left, root.right)]
      while stack:
          left, right = stack.pop()
          if left is None and right is None:#到叶子结点了
              continue
          if left is None or right is None:
              return False
          if left.val == right.val:
              stack.append((left.left, right.right))
              stack.append((left.right, right.left))
          else:
              return False
      return True






