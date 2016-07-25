"""
记原始字符串为s，s的反转字符串为rev_s。

构造字符串l = s + '#' + rev_s，其中'#'为s中不会出现的字符，添加'#'是为了处理输入为空字符串的情形。

对字符串l执行KMP算法，可以得到“部分匹配数组”p（也称“失败函数”）

我们只关心p数组的最后一个值p[-1]，因为它表明了rev_s与s相互匹配的最大前缀长度。

最后只需要将rev_s的前k个字符与原始串s拼接即可，其中k是s的长度len(s)与p[-1]之差。

"""
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[: len(s) - p[-1]] + s
    	