# 本题为求连通图问题。直接用dfs模拟就可以了。
"""
思路：DFS、BFS。只要遍历一遍，碰到一个1，就把它周围所有相连的1都标记为非1，
这样整个遍历过程中碰到的1的个数就是所求解。
"""  	

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = 0
                map(sink,(i,i,i+1,i-1),(j+1,j-1,j,j))#四个方向都考虑
                return 1
            return 0
        
        return sum(sink(i,j) for i in range(len(grid)) for j in range(len(grid[i])))


"""
另一种写法
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
                    
        def set_zero(i,j):
            if 0 <= i < m and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = 0
                map(set_zero,(i,i,i+1,i-1),(j+1,j-1,j,j))
                return 1
            return 0
        
        count = 0
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        for i in range(m):
            for j in range(n):
                count += set_zero(i,j)
        return count


"""
union-find的解法
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    

        if not len(grid): return 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        id = [i for i in range(maxRow * maxCol)]
        self.count = sum([grid[i][j] == '1'  for i in range(maxRow) for j in range(maxCol) ])

        
        def find(x):
            if id[x] != x:
                id[x] = find(id[x])
            return id[x]

        def union(i, j):
            iRoot = find(i)
            jRoot = find(j)
            if iRoot == jRoot:
                return
            else:
                id[iRoot] = jRoot
                self.count -= 1
                

        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j] == '0': continue
                curNode = i * maxCol + j 
                if j < maxCol-1 and grid[i][j+1] == '1':
                    union(curNode, curNode + 1)
                if i < maxRow-1 and grid[i+1][j] == '1':
                    union(curNode, curNode + maxCol)
       return self.count


"""
另一种写法
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            fa_x,fa_y = find(x), find(y)
            if fa_x == fa_y:
                return 
            parent[fa_x] = fa_y
            self.count -= 1
                
                
        if len(grid)==0:return 0        
        row = len(grid); col = len(grid[0])
        parent = [i for i in range(row*col)]
        self.count = sum([grid[i][j]=='1' for i in range(row) for j in range(col)])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                curNode = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(curNode,curNode+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(curNode,curNode+col)
        return self.count


"""
另一种写法
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return 0
            parent[xroot] = yroot
            return 1
        
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        parent = range(m*n)
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    total += 1
        
             
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue    
                cur = i*n + j
                if j < n-1 and grid[i][j+1] == '1': #坐标从2d转向了1D
                    total -= union(cur,cur+1)
                if i < m-1 and grid[i+1][j] == '1':
                    total -= union(cur,cur+n)
                
        return total

