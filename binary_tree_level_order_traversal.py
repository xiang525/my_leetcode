#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Date    : 2015-05-30 22:52:37
# @Author  : Xiang Zuo
# @Email   : xianguo2012@gmail.com
# @Version : 1.0


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root):
        levels, result = [[root]], []

        while levels:
            curLevel = levels.pop()
            newLevel, curValues = [], []
            for node in curLevel:
                if node:
                    curValues.append(node.val)
                    newLevel += [node.left, node.right]
                    print newLevel

            if newLevel:
                levels.append(newLevel)
            if curValues:
                result.append(curValues)

        return result


# The flowing solution using BFS that is much easier to understand
class Solution_BFS:

    def levelOrder(self,root):

        res,next =[],[]
        if root:
            temp=[root]

        else:
            return res
        res.append(temp)
        while 1:
            for v in temp:
                if v.left:
                    next.append(v.left)                
                if v.right:
                    next.append(v.right)
            if next==[]:
                break
            res.append(next)            
            temp=list(next)
            next=[]
        return [[v.val for v in x] for x in res]




# *********** The Second Time ****************
"""
# Solution: 先遍历，记录下每个节点在第几层，然后按层输出。
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
    def preOrder(self,root,level): # 遍历得到层
        if level in Solution.d:
            Solution.d[level].append(root.val)
        else:
            Solution.d[level] = [root.val]
        if root.left:
            self.preOrder(root.left,level+1)
        if root.right:
            self.preOrder(root.right,level+1)
        return

    def levelOrder(self, root):
        res = []
        if not root:
            return res
        Solution.d = {}
        self.preOrder(root,0)
        for i in sorted(Solution.d.keys()):  # 按层输出
            res.append(Solution.d[i])
        return res


"""
九章的写法:BFS 用一个queue和queue的size来实现
这个思想就是先遍历每一层记录这一层的结点， 然后加入result， 很赞的写法
"""
class Solution(object):
    def levelOrder(self,root):
        result = []
        if not root:return result
        queue = []
        queue.append(root)
        while queue:
            level = []
            size = len(queue)
            for i in range(size):                
                head = queue.pop(0) #关键是从前面出站每次！！！
                level.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            
            result.append(level)
        return result


"""
以下做法是行不通的：e.g., [1,2,3,4,5] --> [[1],[2,4],[5,3]]
expected answer: [[1],[2,3],[4,5]]
因为前面没出完， 后面就已经又压入新的元素了，造成混乱！！！
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        stack = [root];ans = []
        while stack:
            size = len(stack)
            tmp = []
            for i in range(size):
                pop = stack.pop()                
                tmp.append(pop.val)
                if pop.right:
                    stack.append(pop.right)
                if pop.left:
                    stack.append(pop.left)
            ans.append(tmp)
        return ans







if __name__ == '__main__':
    tree = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    # a = Solution()
    # print a.levelOrder(node)
    b = Solution_BFS()
    print b.levelOrder(tree)








