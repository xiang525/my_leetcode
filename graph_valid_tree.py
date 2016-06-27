"""
Union Find: compare to a graph, a tree has n-1 edges
"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
    
        parent = range(n)
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
            
        for x,y in edges:
            x, y = find(x),find(y)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1
        