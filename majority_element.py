import math

class Solution:
    # @param {integer[]} nums
    # @return {integer}

    # 解法1
    def majorityElement(self, nums):
		freq = len(nums)/2		
		major_elem = []
		d = {}
		for item in nums:
			d.setdefault(item,[]).append(1)
		for key in d:
			if len(d[key]) >= freq:
				return key


    # 解法2
    def majorityElement(self, num):
	   	num.sort()	   
	   	return num[int(len(num)/2)]



#******** The Second Time **********
"""
解法不是最优O(nlogn)
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
    	nums.sort()
    	return nums[len(nums)/2]

    	

"""The Third Time
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        if nums == []:return None
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key in d:
            if d[key] > len(nums)/2:
                return key
        return None



"""
jiuzhang O(n) solution:出来打架， 一个对一个， 最后剩的就是majority majority element
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        candidate = None;count = 0
        for i in range(0,len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate









    			


if __name__ == '__main__':
	b = Solution()
	array = [8,8,7,7,7,8]

	print b.majorityElement(array)
	print b.majorityElement2(array)



