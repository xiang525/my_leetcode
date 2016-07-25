"""
Union Find 
"""

class Solution(object):
    def countComponents(self, n, edges):
        def find(x): # 找祖先
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xRoot, yRoot = find(x), find(y)
            if xRoot == yRoot: 
                return 0
            parent[xRoot] = yRoot
            return 1

        parent = range(n)
        return n - sum(union(x, y) for x, y in edges) #点的个数 - 边数就是连通分量的个数


"""
DFS
"""
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(graph, visited, i):
            if visited[i] == True:
                return
            visited[i] = True
            for e in graph[i]:
                dfs(graph, visited, e)
        
        visited = [False]*n
        graph = {x:[] for x in xrange(n)}
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        cc = 0
        for i in xrange(n):
            if not visited[i]:
                dfs(graph, visited, i)
                cc += 1
        return cc


"""
BFS
"""
def countComponents(n, edges):
    g = {x:[] for x in xrange(n)}
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    ret = 0
    for i in xrange(n):
        queue = [i]
        ret += 1 if i in g else 0
        for j in queue:
            if j in g:
                queue += g[j]
                del g[j]

    return ret




        