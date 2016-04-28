    class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff=100000
        res=0
        
        for i in range(len(num)):
            left=i+1; right=len(num)-1
            while left < right:
                sum=num[i]+num[left]+num[right]
                diff = abs(sum-target)
                if diff < mindiff: 
                    mindiff = diff;res=sum
                if sum==target: 
                    return sum
                elif sum < target: 
                    left+=1
                else: 
                    right-=1
        return res


# ******** The Second Time **********
"""
# 解题思路：使用一个变量mindiff来监测和与target之间的差值，如果差值为0，直接返回sum值。
# 设置左右两个指针, 用了binary search的思想
# 此方法比上面方法速度快点 O(nlogn)
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff=100000
        res=0
        
        for i in range(len(num)):
            left=i+1; right=len(num)-1
            while left < right:
                sum=num[i]+num[left]+num[right]
                diff = abs(sum-target)
                if diff < mindiff: 
                    mindiff = diff;res=sum
                if sum==target: 
                    return sum
                elif sum < target: 
                    left+=1
                else: 
                    right-=1
        return res


"""
My own solution
"""
def threeSumClosest(self, num, target):
    nums.sort()
    n = len(nums);sums = 0;mindiff = (1<<31);ans = 0
    for i in range(n):
        left = i+1;right = n-1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            diff = abs(sums - target)
            if mindiff > diff:
                mindiff = diff
                ans = sums
            if sums == target:
                return sums
            elif sums > target: #这里不能用diff > 0来判断以为diff是绝对值无法知道是>target or <target
                right -= 1
            else:
                left += 1
    return ans










