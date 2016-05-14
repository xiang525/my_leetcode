import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            shift = tuple([(ord(e) - ord(s[0])) % 26 for e in s])
            d[shift].append(s)
        
        return map(sorted, d.values()) #要排序