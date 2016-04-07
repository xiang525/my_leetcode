# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
    	self.stack = []
    	self.pushLeft(root)

    def pushLeft(self,node):
    	while node: 
    		self.stack.append(node)
    		node = node.left

    def hasNext(self):
    	return self.stack

    def next(self):
    	top = self.stack.pop()
    	self.pushLeft(top.right)
    	return top.val


#  http://bookshadow.com/weblog/2014/12/31/leetcode-binary-search-tree-iterator/

#******** The Second Time *************
"""
# 解题思路：
# 维护一个栈，从根节点开始，每次迭代地将根节点的左孩子压入栈，直到左孩子为空为止。
# 调用next()方法时，弹出栈顶，如果被弹出的元素拥有右孩子，则以右孩子为根，将其左孩子迭代压栈。
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
        

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right) # 要赶紧压入top.right,因为pushLeft只压入了左边的结点
        return top.val

    def pushLeft(self,node):
        while node:
            self.stack.append(node)
            node = node.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


"""
discussion里的解法， good！
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val



























