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
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self,head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
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
九章hashmap 的解法
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:return None
        d = dict()
        dummy = ListNode(0);pre = dummy
        while head:
            if head in d:
                newNode = d[head]
            else:
                newNode = RandomListNode(head.label)
                d[head] = newNode
            pre.next = newNode

            if head.random:
                if head.random in d:
                    newNode.random = d[head.random]
                else:
                    newNode.random = RandomListNode(head.random.label)
                    d[head.random] = newNode.random
            pre = newNode
            head = head.next
        return dummy.next


"""
hash map soluton, O(n) and O(n) space
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        nodeDict = dict()
        dummy = RandomListNode(0)
        pointer, newHead = head, dummy
        while pointer:
            newNode = RandomListNode(pointer.label)
            nodeDict[pointer] = newHead.next = newNode
            newHead, pointer = newHead.next, pointer.next
        pointer, newHead = head, dummy.next
        while pointer:
            if pointer.random:
                newHead.random = nodeDict[pointer.random]
            pointer, newHead = pointer.next, newHead.next
        return dummy.next











