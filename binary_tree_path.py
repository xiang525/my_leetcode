"""
网上的解法
"""

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


"""
My own solution 
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        Solution.ans = []
        self.paths(root,'')
        return Solution.ans
        
    def paths(self,root,tmp):
        if not root:return []
        tmp += str(root.val) + '->'
        if not root.left and not root.right:            
            Solution.ans.append(tmp[:-2])
        return self.paths(root.left,tmp) + self.paths(root.right,tmp)


"""
另一种写法 DFS 
"""

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def dfs(root,path):
            if not root: return []
            path +=  '->' +str(root.val)#'->'占两格
            if not root.left and not root.right:
                ans.append(path[2:])
            return dfs(root.left,path) + dfs(root.right,path)# 凡是求path的都是left+right
        
        ans = []
        dfs(root,'')
        return ans



        