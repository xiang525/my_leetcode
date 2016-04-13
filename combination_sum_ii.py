class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    
	def DFS(self, candidates, target, start, valuelist):
    length = len(candidates)
    if target == 0 and valuelist not in Solution.ret: return Solution.ret.append(valuelist)
    for i in range(start, length):
        if target < candidates[i]:
            return
        self.DFS(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


"""
My own Solution
"""
# ********* The third Time *********************
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(candidates,target,depth,value):
            if target == 0 and value not in ans:
                return ans.append(value)
            for i in range(depth,len(candidates)):
                if target < candidates[i]:return 
                dfs(candidates,target-candidates[i],i+1,value+[candidates[i]])
        ans = []
        candidates.sort()
        dfs(candidates,target,0,[])
        return ans


"""
另一种思路， 写法很相似
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start,sums,value):
            if sums == target and value not in ans:
                ans.append(value)
            for i in range(start,len(candidates)):
                if candidates[i] > target - sums:return
                dfs(i+1,sums+candidates[i],value+[candidates[i]])
                
        ans = []
        candidates.sort()
        dfs(0,0,[])
        return ans




        
