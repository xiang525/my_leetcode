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






        
