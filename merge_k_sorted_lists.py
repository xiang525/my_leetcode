"""
# 典型的使用heap数据结构的题目
# 解题思路：归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，
# 然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，最终形成的链表就是归并好的链表。
如果不用priority queue, O(nk), heap improves it to O(nlogk).
记住从n个数里取一个最大或最小值， 最快的是heap（大顶堆或小顶堆）O(1).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
"""
# 用最小堆, 每个list有一个指针, k个指针放入堆中, 每次pop出最小的, 然后指向相应list的下一个node, 再push入堆。
# 最小堆是一个数组, 所有元素满足heap[k] <= heap[2*k+1]和heap[k] <= heap[2*k+2], heap[0]即堆顶最小。
# Python堆操作真方便:
# heapq.heapify(a) 把list a中元素调换顺序使其成为最小堆, a还是list
# heapq.heappush(a, (10, sth_else))  把(10, sth_else)插入堆a中, a仍为最小堆, 也可以只插入数10
# heapq.heappop(a) 弹出堆顶元素, a中的最小值
# heapq.heappushpop(a, (10, sth_else)) 先push再pop, 效率比依次调用heappush()和heappop()高 
"""


"""
merge two by two
solution in discussion
O(nlogk)
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:return None
        if len(lists) == 1:return lists[0]
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left,right)
                
        
    def merge(self,head1,head2):
        dummy = ListNode(0); p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                p = p.next
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return dummy.next


"""
另一种写法
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0); p = dummy
        heap = []
        for e in lists:
            if e:
                heap.append((e.val,e)) #如果不push e.val没法pop出最小的值，需要一个数值用于建最小堆
        heapq.heapify(heap)
        while heap:
            pop = heapq.heappop(heap)
            p.next = ListNode(pop[0]) # p.next = pop[1]
            p = p.next
            if pop[1].next:
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
        return dummy.next











