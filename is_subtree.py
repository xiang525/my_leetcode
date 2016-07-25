"""
Check if a binary tree is subtree of another binary tree | Set 1
Given two binary trees, check if the first tree is subtree of the second one. 
A subtree of a tree T is a tree S consisting of a node in T and all of its descendants 
in T. The subtree corresponding to the root node is the entire tree; the subtree 
corresponding to any other node is called a proper subtree.
"""
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def isIdential(self, root1, root2):
		if not root1 and not root2:
			return True
		if not root1 or not root2:
			return False
		return (root1.val == root2.val) and self.isIdential(root1.left, root2.left) \
		and self.isIdential(root1.right, root2.right) 

	def isSubtree(self, S, T):
		if S is None or T is None: return True
		if self.isIdential(S, T):
			return True
		return self.isSubtree(S, T.left) or self.isSubtree(S, T.right)


"""
"""
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


	def isIdentical(self, root1, root2):
		if root1 is None and root2 is None: return True
		if root1 is None or root2 is None: return False
		return (root1.val == root2.val) and self.isIdentical(root1.left, root2.left) and 
				self.isIdential(root1.right, root2.right)

	def isSubtree(self, S, T):
		if S is None: return True
		if T is None: return True
		if self.isIdential(S, T): return True
		return self.isIdentical(S, T.left) or self.isIdentical(S, T.right)
		










