"""
O(n) space不是最优解
"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.stack = [x for row in vec2d for x in row]#就是下面几行的意思
        # for e in vec2d:
        #     size = len(e)
        #     for i in range(size):
        #         self.stack.append(e[i])
        

    def next(self):
        """
        :rtype: int
        """
        while self.hasNext():
            return self.stack.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        return True
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


"""
O(1) space，注意下调用的形式
用row 和col可以解决找vector里每一个值的问题，这样就不用存储所有的了
"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.col = 0
        self.row = 0
        self.vec = vec2d
        

    def next(self):
        """
        :rtype: int
        """
        val = self.vec[self.row][self.col]
        self.col += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec):
            while self.col < len(self.vec[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False
            
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())




