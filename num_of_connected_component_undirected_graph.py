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
        return n - sum(union(x, y) for x, y in edges)