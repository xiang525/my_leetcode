class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
       
        self.ans = []
        self.factor = []
        self.cla_fac(n)

        self.dfs( n, [])
        if self.ans == [[]]:
            return []
        return self.ans

    def dfs(self, n, tmpAns):
        if n == 1:
            self.ans.append(tmpAns)
            return
        for f in self.factor:
            if n%f == 0:
                if tmpAns and tmpAns[-1] > f:
                    continue
                self.dfs(n/f, tmpAns + [f])

    def cla_fac(self, n):
        for i in xrange(2, n):
            if n%i == 0:
                self.factor.append(i)


"""
另一种写法
"""
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
       
        
        def dfs(n, value):
            if n == 1:
                ans.append(value)
                return
            for f in factor:
                if n%f == 0: #每一次循环后n都改变了
                    if value and value[-1] > f:
                        continue
                    dfs(n/f, value + [f])

        def helper(n):
            for i in xrange(2, n):# 这里用range过不去
                if n%i == 0:
                    factor.append(i)
                    
        ans = []
        factor = []
        helper(n)
        dfs(n, [])
        if ans == [[]]:
            return []
        return ans

