class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for e in strs:
            res += str(len(e)) +':' + e
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            index = s.find(':',i) # i is the begin position
            size = int(s[i:index])
            #size = int(s[index-1]) # 不能处理两位数, 因为不止一位， e.g., 12
            strs.append(s[index+1:index+1+size])
            i = index+1+size
        return strs