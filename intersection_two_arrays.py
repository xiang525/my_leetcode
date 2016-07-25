class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1=set(nums1)
    nums2=set(nums2)
    return list(nums1&nums2)

"""
此题解法很多
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


"""
two pointers
"""
class Solution(object):
    def intersection(self, nums1, nums2):
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
            else: #这里有多重解法来去重
                #if not (len(res) and nums1[i] == res[len(res)-1]):
                #if not res or (res and nums1[i] not in res):
                if nums1[i] not in res:
                    res.append(nums1[i])
                i += 1
                j += 1
    
        return res