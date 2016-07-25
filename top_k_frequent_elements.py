"""
O(n+klogn)
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}; ans = []
        heap = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for key in d:
            heapq.heappush(heap,(-d[key], key))
        heapq.heapify(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
        