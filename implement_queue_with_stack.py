"""
这个做法有些作弊，不提倡
"""

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        

    # @return nothing
    def pop(self):
        self.stack.pop(0)
        

    # @return an integer
    def peek(self):
        return self.stack[0]
        

    # @return an boolean
    def empty(self):
        return self.stack == []


"""
九章两个stack的解法;注意细节
"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        
    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.adjust()
        self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.adjust()
        return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.stack1) and (not self.stack2)



"""
My own solution
"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.reverseStack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.reverseStack:#如果不为空push进去后元素顺序就乱了所以只在为空的时候push
            while self.stack:
                self.reverseStack.append(self.stack.pop())
        self.reverseStack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.reverseStack:
            while self.stack:
                self.reverseStack.append(self.stack.pop())
        return self.reverseStack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.reverseStack) and (not self.stack)#两个stack都为空时才空

        