class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


	def encode(self, root, struc, data):
		if not root:
			struc.append(0)
			return
		struc.append(1)
		data.append(root.key)
		self.encode(root.left, struc, data)
		self.encode(root.right, struc, data)


	def decode(self, struc, data):
		if not struc:
			return None
		tmp = struc.pop(0)
		if tmp == 1:
			root = Node(data.pop(0))
			root.left = self.decode(struc, data)
			root.right = self.decode(struc, data)
			return root
		return None 

	def printTree(root):
		if root:
			print root.val
			self.printTree(root.left)
			self.printTree(root.right)


"""
write it again 
"""
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def encode(self, root, structure, data):
		if not root:
			structure.append(0)
			return
		structure.append(1)
		data.append(root.val)
		self.encode(root.left, structure, data)
		self.encode(root.right, structure, data)

	def decode(self, structure, data):
		if not structure: return None
		tmp = structure.pop(0)
		if tmp == 1:
			root = Node(data.pop(0))
			root.left = self.decode(structure, data)
			root.right = self.decode(structure, data)
			return root
		return None

	def printTree(self, root):
		if root:
			print root.val
			self.printTree(root.left)
			self.printTree(root.right)









