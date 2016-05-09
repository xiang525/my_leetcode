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
                ans.append(str(root.val))
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