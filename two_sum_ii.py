
"""
two pointers O(n)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0; right = n -1
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return left+1, right+1
            elif sums > target:
                right -= 1
            else:
                left += 1

"""
dictionary O(n)
"""
          
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i