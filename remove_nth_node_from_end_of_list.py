# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	dummyHead = ListNode(0)   # what does ListNode(0) mean?
        dummyHead.next = head
        slow = fast = dummyHead

        for i in range(n):  # move to the deletion position
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyHead.next


# ********************** The Second Time ***************
"""
# solution: using two pointers, one moves n steps first and then two move together. 
# When the first pointer reaches the end of the list, the position of the second pointer
# is where we need to delete the element.
"""

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next



# ************ My own solution *************
# two pointers
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        if not head.next and n ==1:return []
        dummy = ListNode(0); p = dummy; dummy.next = head
        
        while p:
            p1 = p
            for i in range(n):
                p1 = p1.next
            if p1.next == None:
                p.next = p.next.next
                return dummy.next
            else:
                p = p.next



















