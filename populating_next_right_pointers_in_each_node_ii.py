# 解题思路：和"Populating Next Right Pointers in Each Node"这道题不同的一点是，
# 这道题的二叉树不是满的二叉树，有些节点是没有的。但是也可以按照递归的思路来完成。在编写递归的基准情况时
# 需要将细节都考虑清楚：

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
    	if root:
    		if root.left and root.right:
    			root.left.next = root.right
    			tmp = root.next
    		while tmp:
    			if tmp.left:
    				root.right.next = tmp.left
    				break
    			if tmp.right:
    				root.right.next = tmp.right
    				break
    			tmp = tmp.next
    		elif root.left:
    			tmp = root.next
    			while tmp:
    				if tmp.left:
    					root.left.next = tmp.left
    					break
    				if tmp.right:
    					root.left.next = tmp.right
    					break
    				tmp = tmp.next
    		elif root.right:
    			while tmp:
    				if tmp.left: 
    					root.right.next = tmp.left
    					break
    				if tmp.right:
    					root.right.next = tmp.right
    					break
    				tmp = tmp.next
    		self.connect(root.right)
    		self.connect(root.left)


#  没看懂以下写法？？？？？？
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
    	if root:
            p = root; q = None; nextNode = None
            while p:
                if p.left:
                    if q: 
                    	q.next = p.left
                    q = p.left
                    if nextNode == None: 
                    	nextNode = q
                if p.right:
                    if q: 
                    	q.next = p.right
                    q = p.right
                    if nextNode == None: 
                    	nextNode = q
                p = p.next
            self.connect(nextNode)


























