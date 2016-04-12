class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses; 
        indegree = [0]*n
        childs = [[] for i in range(n)]
        print childs 
        # childs = {}
        if not prerequisites: return True
        
       
        for e in prerequisites:            
            indegree[e[0]] += 1           
            childs[e[1]].append(e[0])
        print childs,indegree 

        k = 0; stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            tmp = stack.pop()
            k += 1            
            for ee in childs[tmp]:
                indegree[ee] -= 1
                if indegree[ee] == 0:
                    stack.append(ee)
        return numCourses==k



if __name__ == '__main__':
    a = Solution()
    print a.canFinish(3,[[1,0],[2,0]])







