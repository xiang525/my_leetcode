class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
    	candidates.sort()
    	solution.net = []
    	self.DFS(candidates,target,0,[])
    	return solution.net

    def DFS(self,candidates,target,start,valuelist):
    	length = len(candidates)
    	if target == 0:
    		return solution.net.append(valuelist)
    	for i in range(start,length):
    		if target < candidates[i]:  # cannot find then return to terminate
    			return 
    		self.DFS(candidates,target-candidates[i],i,valuelist+[candidates[i]])


"""
穷举的时候一般考虑DFS，DFS就是递归
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ans = []
        self.dfs(candidates,target,0,[])
        return Solution.ans

    def dfs(self,candidates,target,start,value):
        n = len(candidates)
        if target == 0:
            Solution.ans.append(value)
        for i in range(start,n):
            if target < candidates[i]:
                return
            self.dfs(candidates,target-candidates[i],i,value+[candidates[i]])



# ********* The Third Time *********

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,target,start,value):
            if target == 0:
                ans.append(value)
            for i in range(start,len(candidates)):
                if target < candidates[i]:
                    return
                dfs(candidates,target-candidates[i],i,value+[candidates[i]])
                
        candidates.sort()  #关键在sort
        ans = []
        dfs(candidates,target,0,[])
        return ans



# my own solution
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,sums,target,start,value):
            if sums == target:
                res.append(value)
            for i in range(start,len(candidates)):
                if candidates[i] > target - sums:return  # 关键在这，递归要有终止条件
                dfs(candidates,sums+candidates[i],target,i,value+[candidates[i]])
        
        candidates.sort()
        res = []
        dfs(candidates,0,target,0,[])
        return res


"""
可以这样写
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start,target,value):
            if target == 0:
                ans.append(value)
            for i in range(start,len(candidates)):
                if target < candidates[i]:
                    break
                dfs(i,target-candidates[i],value+[candidates[i]]) # 这里i不是i+1, 因为同一个数可以被无数次的选择
        ans = []
        candidates.sort() # 一个关键点
        dfs(0,target,[])
        return ans

"""
另一种写法
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start,value):
            if sum(value) == target:
                ans.append(value)
                return
            for i in range(start,len(candidates)):
                if sum(value) + candidates[i] > target: return
                dfs(i,value+[candidates[i]])
                
        ans = []
        candidates.sort()
        dfs(0,[])
        return ans








            

