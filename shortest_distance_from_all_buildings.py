class Solution(object):
    def shortestDistance(self, grid):
    """
    """    
    ## do BFS from each building, and decrement all empty place for every building visit
    ## when grid[i][j] == -totalB, it means that grid[i][j] are already visited from all buildings
    ## and use dist to record distances from buildings
        def bfs(i, j, bIndex):
            queue = collections.deque([(i, j, 0)])
            while queue:
                i, j, d = queue.popleft()
                for x,y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0<=x<m and 0<=y<n and grid[x][y] == bIndex:#bIndex是剪纸用的， 凡是每次bIndex不-1 的话不考虑


                        dist[x][y] += d+1
                        grid[x][y] -= 1
                        queue.append((x, y, d+1))
                        
                        
                        
        m = len(grid); n = len(grid[0])        
        if not m or not n:
            return -1
        dist = [[0]*n for i in range(m)]
        totalB = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    totalB += 1 # record # of buildings

        bIndex = 0 #用来剪枝 bfs
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    bfs(i, j, bIndex)
                    bIndex -= 1
                    
        res = [dist[i][j] for i in range(m) for j in range(n) if grid[i][j]+totalB==0]
        return min(res) if res else -1




        