# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
            
                
"""
另一种写法
两个指针
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p = head; q = head.next
        while p and q:
            if p.val == q.val:
                while p and q and p.val == q.val:
                    q = q.next
                p.next = q
            else:
                p = p.next
                q = q.next
        return head            
                
                
            
            
            
        