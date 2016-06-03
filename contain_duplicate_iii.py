"""
# 一个简单的解法， 从discussion中找到的
# 此题有用bucket实现的， 可以想想
Index 被改变了， 为啥还可以？？？？
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
    	ind = sorted(range(len(nums)),key=lambda x: nums[x]) # 得到index
        # input [7,5,34,6] ind: [1,3,0,2]
    	# 根据nums中值的大小排序后记录index  
        print 'ind: ',ind  	
    	for i in range(len(nums)-1):
    		j = i + 1
    		# print 'i,j,ind[i],ind[j]:',i,j,ind[i],ind[j]
    		while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
    			if abs(ind[i] - ind[j]) <= k:
    				return True
    			j += 1
    	return False


"""
论坛里桶排序的解法
非常好！
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False # 可以保证下面的w != 0
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: 
                del d[nums[i - k] / w]
        return False


"""
另一种写法
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        bucket = {}; n = len(nums)
        w = t+1
        for i in xrange(n):
            m = nums[i] / w
            if m in bucket: return True
            if m-1 in bucket and abs(nums[i]-bucket[m-1]) <= t: return True
            if m+1 in bucket and abs(nums[i] -bucket[m+1]) <= t: return True
            bucket[m] = nums[i]
            if i >= k:
                del bucket[nums[i-k]/w]
        return False
            




if __name__ == '__main__':
 	a = Solution()
 	a.containsNearbyAlmostDuplicate([4,2,1],2,1)

