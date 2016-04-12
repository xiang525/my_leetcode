"""
# 此问题等价于寻找有向图的拓扑顺序。如果存在环路，不存在拓扑顺序，也就不可能修完所有的课程。
# 通过DFS实现的拓扑排序
# 以下算法很好,实现了经典的拓扑排序
flag用来控制死循环, e.g., 2, [[0,1],[1,0]]), 没有degree == 0的， 循环就会死下去
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degrees = [0] * numCourses
        childs = [[] for i in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1  # in-degree
            childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))  # initialize courses with the size of course; courses = set([0,1,2,3])
        flag = True  # flag is used to control finding nodes with zero in-degree. 
        ans = []
        while flag and len(courses):
            flag = False
            removeList = []
            for i in courses:
                if degrees[i] == 0:
                    for child in childs[i]:
                        degrees[child] -= 1
                    removeList.append(i)
                    flag = True
            for j in removeList:
                ans.append(j)
                courses.remove(j)
        return [[], ans][len(courses) == 0]

"""
My own solution extends from 207
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses; indegree = [0]*n; childs = [[] for i in range(n)] 
        for e in prerequisites:
            indegree[e[0]] += 1
            childs[e[1]].append(e[0])
            
        k = 0; stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)
        ans = []
        while stack:
            tmp = stack.pop()
            k += 1
            if tmp not in ans:
                ans.append(tmp)
            for ee in childs[tmp]:
                indegree[ee] -= 1
                if indegree[ee] == 0:
                    stack.append(ee)
                    
        return [[],ans][k==n]




        