"""
# 解题思路：这道题和层序遍历那道题差不多，区别只是在于奇数层的节点要翻转过来存入数组。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def preorder(self,root,level,res):
    	if root:
    		if len(res) < level + 1:
    			res.append([])  # because of returning [][]???
    		if level % 2==0:  # even level
    			res[level].append(root.val) # 因为总是在首位插入， 所以是先right后left
    		else:
    			res[level].insert(0,root.val)  # level说明在哪个位置插入
    		self.preorder(root.left,level+1,res)
    		self.preorder(root.right,level+1,res)

    def zigzagLevelOrder(self, root):
    	res = []
    	self.preorder(root,0,res)
    	return res

"""
另一种写法
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(root,level):
            if root:
                if len(ans) < level + 1:
                    ans.append([])
                if level % 2 == 0:
                    ans[level].append(root.val)
                else:
                    ans[level].insert(0,root.val)
                
                bfs(root.left,level+1)
                bfs(root.right,level+1)
            
        ans = []
        if not root: return []
        bfs(root,0)
        return ans



"""
非递归的BFS写法
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans = []; stack = [root]; level = 0
        while stack:
            print level
            tmp = []
            size = len(stack)
            for i in range(size):
                pop = stack.pop(0)
                if level % 2 == 0:
                    tmp.append(pop.val)
                else:
                    tmp.insert(0,pop.val)
                if pop.left:
                    stack.append(pop.left)
                if pop.right:
                    stack.append(pop.right)
            level += 1
            ans.append(tmp)
        return ans



