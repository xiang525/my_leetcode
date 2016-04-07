class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):    	
    	nums.sort() 
        res = []
        res.append([])
        for num in nums:
            n = len(res)
            for i in range(n):
                temp = list(res[i])
                temp.append(num)  
                res.append(temp)
        return res

# the second solution

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        if S == []:
            return []
        S.sort() #sort the array to avoid descending list of int
        res=[[]]
        for element in S:
            temp = []
            for ans in res:
                 #append the new int to each existing list
                temp.append(ans+[element])
            res += temp
        return res



"""
# ******** The Second Time **********
# 题意：枚举所有子集。碰到这种问题，一律dfs。
# 对于输入字符串s的每一位字符, 选取该字符到子集合中，并输出;如果，当前字符不是最后一位字符
# 递归调用Generate,处理下一位字符.
# rescusive
# 总结：permutation, subset有一套现成的递归、回溯模板，同学们一定要多加练习，练多了才能做到bug free，
# 否则面试时有些地方没有考虑全，出现bug就会跪掉哦！
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        def dfs(depth,start,valuelist):
            res.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,valuelist+[nums[i]])
        nums.sort() #sort the array to avoid descending list of int
        res = []
        dfs(0,0,[])
        return res


# ********* The Second Time *********
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        
        def dfs(depth,start,value):
            ans.append(value)
            if depth == len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,value+[nums[i]])
        nums.sort()
        ans = []
        dfs(0,0,[])
        return ans

# 经典题必会






























