import collections
class Solution(object):  
    def groupStrings(self, strings):  
        """ 
        :type strings: List[str] 
        :rtype: List[List[str]] 
        """  
        d = collections.defaultdict(list)  
        for s in strings:  
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s]) 
            print ord(c), ord(s[0]),shift 
            d[shift].append(s)  
          
        return map(sorted, d.values()) 
           
        
              


if __name__ == '__main__':
    a = Solution()
    print a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])









