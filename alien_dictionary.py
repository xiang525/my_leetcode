"""
论坛里的解法， 关键是zip()用的很好
"""
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        chars = set("".join(words))
        degrees = {x:0 for x in chars}
        graph = collections.defaultdict(list)
        for pair in zip(words, words[1:]):
            for x, y in zip(*pair):
                if x != y:
                    graph[x].append(y)
                    degrees[y] += 1
                    break

        queue = filter(lambda x: degrees[x] == 0, degrees.keys())
        ret = ""
        while queue:
            x = queue.pop()
            ret += x
            for n in graph[x]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    queue.append(n)

        return ret * (set(ret) == chars)