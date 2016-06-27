"""
O(n) without extra space
最优解法
由于output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)
因此执行两趟循环：
第一趟正向遍历数组，计算x0 ~ xi-1的乘积
第二趟反向遍历数组，计算xi+1 ~ xn-1的乘积
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums); res = [0]*n
        res[0] = 1
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(n-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res



"""
另一种写法
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums); res = [1]*n
        left = 1
        for i in range(n-1):
            left *= nums[i]
            res[i+1] *= left
        
        right = 1
        for i in range(n-1,0,-1):
            right *= nums[i]
            res[i-1] *= right
        return res


        