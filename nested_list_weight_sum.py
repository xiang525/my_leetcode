"""
论坛里的解法, DFS
"""

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def dfs(nestint,depth):
            if nestint.isInteger():
                return nestint.getInteger() * depth
            else:
                return sum(dfs(e,depth+1) for e in nestint.getList())
        
        return sum(dfs(e,1) for e in nestedList)


"""
BFS
"""
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = 0; depth = 1
        while nestedList:
            stack = []
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    stack.extend(item.getList())
            nestedList = stack
            depth += 1
        return res



        