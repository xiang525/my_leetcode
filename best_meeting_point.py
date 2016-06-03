"""
这一题距离的计算方法其实是x于y分开的，所以我们可以把它分为2个1-D的结果的和。
在X轴的1-D问题上，最佳的meeting point就是所有X坐标的median中间点:
如果是偶数个，只要是中间两个点之间就可以;
如果是奇数个，那就应该是中间那个点.
Actually, there is a famous conclusion in statistics that the median minimizes the 
sum of absolute deviations.
http://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations
O(mn) + O(m+n) space
"""

 Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        row = []; col = []; result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        col.sort()# row里面已经sorted了， 所以只用sort col
        median_row = row[len(row)/2]
        median_col = col[len(col)/2]
        
        for i in row:
            result += abs(i-median_row)
        for i in col:
            result += abs(i-median_col)
        return result
        