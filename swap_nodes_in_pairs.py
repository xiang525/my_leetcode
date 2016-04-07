# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head): 
    	if not head or not head.next:
    		return head
    	dummy = ListNode(0); dummy.next = head
    	p = dummy
    	while p.next and p.next.next:
    		tmp = p.next.next
    		p.next.next = tmp.next
    		tmp.next = p.next
    		p.next = tmp
    		p = p.next.next
    	return dummy.next	
    	
    	
"""
My own solution, swap values instead of pointers
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        p = head
        while p and p.next:
            p.val, p.next.val = p.next.val, p.val
            p = p.next.next
        return head