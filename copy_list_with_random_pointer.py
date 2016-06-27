"""
# 题目给出了一个特殊的单链表。链表的每一个节点多了个指针域: random. 随机指向链表的某一个node。
# 题目要求我们给出这个链表的一个 deep copy.
首先，何为 deep copy ??
Part 1:  三种 Object Copy 的对比(以 Array 为例)
1. Shallow copy
拷贝时仅仅复制的是 指针 或者 引用， 也就是说 数据仅存在一份。
当然，得到效率的同时，存在的问题就是，如果原来的数据改变了， 复制后的对象也改变了，因为仅仅存在一份数据!!!
Note: 其实是出于效率的考虑，在某些场合，并不需要多份数据时，可以采用 shallow copy
2. Deep copy
与 shallow copy 不同，deep copy 复制后，数据有多份。因此， deep copy 也比较费时。
在 C++ 中，可以自行定义类的 copy 构造函数来实现 deep copy.
Python 中，array 默认的复制是 shallow copy,  可以采用 copy 模块的 deep copy

http://blog.csdn.net/shoulinjun/article/details/18730871
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None: return None
        tmp = head
        while tmp: # 这个loop插入相同的节点到原节点后面
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next # 因为复制了一个原节点， 要往后移动2个
        tmp = head
        while tmp: # this loop gives random pointer 
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        # 开始分离一个链表成两个
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None


"""
九章solution, 思路非常清晰，比起hashmap没有耗费过多的空间
O(1) space
算法班 视频5 1:42:16
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:return None
        self.copyNext(head)
        self.copyRandom(head)
        return splitList(head)

        
    def copyNext(self,head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.random = head.random #这是只是为了记录newNode有random以备后面用
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self,head):
        while head:
            if head.next.random: #这里就用到了上面记录的random
                head.next.random = head.random.next#原来的元素后面紧接的是copy的元素，两个random是挨在一起的
            head = head.next.next 

    def splitList(self,head):
        newHead = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            if tmp.next:
                tmp.next = tmp.next.next
        return newHead





"""
hashmap soluton, O(n) and O(n) space
使用哈希表保存原链表到新链表节点的映射，即可实现对随机指针域的拷贝
O(n) loop 2遍， 第一遍存结点的对应关系， 第二遍set random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        dummy = RandomListNode(0)
        p, newhead = head, dummy
        while p:
            newNode = RandomListNode(p.label)
            d[p] = newNode
            newhead.next = newNode
            newhead = newhead.next
            p = p.next
            
        p, newhead = head, dummy.next
        while p:
            if p.random:
                newhead.random = d[p.random]
            p = p.next
            newhead = newhead.next
        return dummy.next











