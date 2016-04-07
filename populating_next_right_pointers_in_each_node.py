# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root and root.left:
    		root.left.next = root.right
    		if root.next:
    			root.right.next = root.next.left
    		else:
    			root.right.next = None
            self.connect(root.left)
            self.connect(root.right)


# ********* The Second Time **********
"""
# 解题思路：看到二叉树我们就想到需要使用递归的思路了
# 一下代码很简洁
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root and root.left:
    		root.left.next = root.right
    		if root.next:
    			root.right.next = root.next.left
    		else:
    			root.right.next = None
    		self.connect(root.left)
    		self.connect(root.right)



























