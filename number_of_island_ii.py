"""
论坛里find_union的解法
"""

class Solution(object):
    def find(self, i,parent):
        if i!=parent[i]:
            parent[i]=self.find(parent[i], parent)
        return parent[i]

    def union(self, i,j, parent):
        root1 = self.find(i,parent)
        root2 = self.find(j, parent)
        if root1 == root2:
            return True
        parent[root1] = root2
        return False

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        result = []
        parent = [-1]*m*n
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        num = 0
        for pos in positions:
            idx = pos[0]*n+pos[1]
            parent[idx] = idx
            num+=1
            for d in dirs:
                i =pos[0]+d[0]
                j = pos[1]+d[1]
                new_idx = i*n+j
                if i<0 or j<0 or i>=m or j>=n or parent[new_idx]==-1:
                    continue
                if not self.union(idx, new_idx, parent):
                    num-=1
            result.append(num)
        return result



"""
另一种写法
"""
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            fx,fy = find(x),find(y)
            if fx == fy: return True
            parent[fx] = fy
            return False
        
        parent = [-1]*(m*n)
        ans = []; num = 0; direct = [(0,1),(0,-1),(-1,0),(1,0)]
        for pair in positions:
            x = pair[0]; y = pair[1]
            index = x*n+y
            parent[index] = index
            num+= 1
            for d in direct:
                i = x+d[0]; j = y+d[1]
                new_index = i*n+j
                if i < 0 or j < 0 or i >= m or j >= n or parent[new_index] == -1:
                    continue
                if not union(new_index,index):
                    num -= 1
            ans.append(num)
        return ans

