"""
# 题意：接上一题，这题要求返回的是所有符合条件的二叉查找树，而上一题要求的是符合条件的二叉查找树的棵数，
# 我们上一题提过，求个数一般思路是动态规划，而枚举的话，我们就考虑dfs了。dfs(start, end)函数返回以
# start，start+1，...，end为根的二叉查找树。
# 递归是关键
递归, 对于[start, end]范围内的每个节点, 产生所有可能的左、右子树, 再产生(#左子树 x #右子树)棵树, 
返回所有的root nodes。gen函数返回一个list of root nodes, 每个root node所表示的树是由
[start, end]这个范围内的数构成的BST。
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Nones

class Solution:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end: 
            return [None]
        res = []
        for rootval in range(start, end+1):　　　　　　　　#rootval为根节点的值，从start遍历到end
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:　　　　　　　　　　　　　　　　#i遍历符合条件的左子树
                for j in RightTree:　　　　　　　　　　　　  #j遍历符合条件的右子树
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        if n == 0:return []
        return self.dfs(1, n)


"""
另一种写法, 思路和95题很类似
"""
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.dfs(1,n)        
        
        
    def dfs(self,start,end):
        if start > end: return [None]
        res = []
        for rootval in range(start,end+1):
            left = self.dfs(start,rootval-1)
            right = self.dfs(rootval+1,end)
            for i in left:
                for j in right:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res







"""
# 以下程序不能通过，因为输出不符合要求， 题目不是要以list 形式输出而是一个一个结果输出

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        def dfs(start,end):
            if start > end: return [None]            
            for rootval in range(start,end+1):
                left = dfs(start,rootval-1)
                right = dfs(rootval+1,end)
                for i in left:
                    for j in right:
                        root = TreeNode(rootval)
                        root.left = i 
                        root.right = j
                        res.append(root)
            
        res = []
        dfs(1,n)
        return res


"""
通过的解法
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(start,end):
            if start > end: return [None] #返回list形式否则后面127 or 128行会出问题
            ans = [] #每次输出以某一个值为root的所以tree后清空，为下个准备，同时这种结构的输出
            for value in range(start,end+1):
                left = dfs(start, value-1)
                right = dfs(value+1, end)
                for i in left:
                    for j in right:
                        root = TreeNode(value)
                        root.left = i
                        root.right = j
                        ans.append(root)
            return ans
        
        if n == 0: return []
        return dfs(1,n)
        

























