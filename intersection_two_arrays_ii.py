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


"""
solution with two pointers 
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else: 
                res.append(nums1[i])
                i += 1
                j += 1
    
        return res


        
        