"""
论坛里的解法
利用字典wmap保存单词 -> 下标的键值对

遍历单词列表words，记当前单词为word，下标为idx：

1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
     
     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mp = {w:i for i, w in enumerate(words)}
        ret = []
        for i, w in enumerate(words):
            for j in xrange(len(w) + 1):
                a = w[:j]
                b = w[j:]                
                if a == a[::-1]:
                    if mp.has_key(b[::-1]) and mp[b[::-1]] != i:
                        ret.append((mp[b[::-1]], i)) #举个例子就知道了

                if b == b[::-1]:
                    if mp.has_key(a[::-1]) and mp[a[::-1]] != i:
                        ret.append((i, mp[a[::-1]]))

        return list(set(ret))




        