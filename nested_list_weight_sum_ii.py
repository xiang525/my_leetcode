"""
BFS: 不直接就权重， 把前面的结果带入后面的计算可实现权重增加
"""
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        unweighted, weighted = 0, 0
        while nestedList:
            stack = []
            for e in nestedList:
                if e.isInteger():
                    unweighted += e.getInteger()
                else:
                    stack.extend(e.getList())
            weighted += unweighted
            nestedList = stack
        return weighted