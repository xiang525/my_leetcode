class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
    	def dfs(start,valuelist):
    		if self.count == k:
    			res.append(valuelist)
    			return
    		for i in range(start,n+1):
    			self.count += 1
    			dfs(i+1,valuelist + [i])
    			self.count -= 1  #如果不减1， count就会一直增加， 但是我们需要count每次从0开始
    	res = []
    	self.count = 0
    	dfs(1,[])
    	return res


 # ********** The Second Time ************
 class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        def dfs(start,value):        
            for i in range(1,n):
                self.count += 1
                if self.count == k:
                    value.append(value)
                dfs(i+1,value+[i])
        ans = []
        self.count = 0
        dfs(0,[])
        return ans
# 解题思路：这种求组合的问题，需要使用dfs来解决。























