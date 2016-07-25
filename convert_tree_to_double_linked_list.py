"""
http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
Tree to doubly linked list
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.right = None

class Conversion:
	def __init__(self):
		self.head = None

	def bintree2listUtil(root, prev):
		if not root: return
		bintree2listUtil(root.left, prev)
		if prev == None:
			self.head = root
		else:
			root.left = prev
			prev.right = root
		prev = root
		bintree2listUtil(root.right, prev)
	return self.head

"""
Tree to doubly circular linked list
"""
class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.right = None

class Conversion:
	def __init__():
		self.head = None

	def treeToDoublyList(root, prev):
		if not root: return
		treeToDoublyList(root.left, prev)
		if prev == None:
			self.head = root		
		else:
			root.left = prev
			prev.right = root		

		# form a circle
		self.head.left = root
		root.right = self.head

		prev = root
		treeToDoublyList(root.right, prev)
		return self.head



	


class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.right = None

class Conversion:
	def __init__(self):
		self.head = None

	def treeToList(self, root, prev):
		if not root: return
		self.treeToList(root.left)
		if prev == None:
			self.head = root
		else:
			root.prev = prev
			prev.right = root

		self.head.prev = root
		root.right = self.head

		prev = root
		self.treeToList(root.right)
		return self.head 



























