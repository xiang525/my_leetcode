import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        chars = set("".join(words))        
        degrees = {x:0 for x in chars}
        graph = collections.defaultdict(list)
        print words, words[1:],zip(words, words[1:])
        for pair in zip(words, words[1:]):
            for x, y in zip(*pair):
                print pair, zip(*pair)
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
           
        
              


if __name__ == '__main__':
    a = Solution()   
    print a.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])







