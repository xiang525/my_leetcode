class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        d = {}
        for e in nums1:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        
        for e in nums2:
            if e in d.keys() and d[e] > 0: #关键在这两行
                ans.append(e)
                d[e] -= 1
        return ans