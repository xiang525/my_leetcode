# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                ans.append(str(root.val)) #要先序遍历否则decode的时候不好找root
                helper(root.left)
                helper(root.right)
            else:
                ans.append('#')
        ans = []
        helper(root)
        return ' '.join(ans)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper2():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper2()
            node.right = helper2()
            return node
            
        vals = iter(data.split())
        return helper2()


"""
论坛里的另外一种解法
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                ans.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                ans.append('#')
            
        ans = []
        helper(root)
        return ' '.join(ans)
        

    
    def deserialize(self, encode_data):
        pos = -1
        #if not encode_data: return None
        data = encode_data.split(' ')
        for i in xrange(len(data)):
            if data[i] == '#':
                data[i] = None
            else:
                data[i] = int(data[i])
        root, count = self.buildTree(data, pos)
        return root

    def buildTree(self, data, i):
        i += 1
        if i >= len(data) or data[i] == None:
            return None, i
        root = TreeNode(data[i])
        root.left, i = self.buildTree(data, i)
        root.right, i = self.buildTree(data, i)
        return root, i



"""
我自己的写法思路和上面一样
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root:
                ans.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                ans.append('#')
        ans = []
        preorder(root)
        return ' '.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pos = 0
        newData = data.split(' ')
        for i in range(len(newData)):
            if newData[i] == '#':
                newData[i] = None
            else:
                newData[i] = int(newData[i])
        root, position = self.buildTree(newData,pos)
        return root
        
        
    def buildTree(self,data,pos):
        if pos >= len(data) or data[pos] == None:
            return None, pos
        root = TreeNode(data[pos])
        root.left, pos = self.buildTree(data,pos+1)# 不返回的话pos的值不会改变无法遍历后面的数组
        root.right, pos = self.buildTree(data,pos+1)
        return root, pos








