# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
    	
		dummy = ListNode(0)  # creat a listnode 
		dummy.next = head
		pre, current = dummy, head
		while current:
			if current.val == val:
				pre.next = current.next
			else:
				pre = current
			current = current.next
		return dummy.next




# ************* The Second Time ********************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Solution: two pointers, pre and cur.
class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
    	dummy = ListNode(0)
    	dummy.next = head
    	pre,cur = dummy, head
    	while cur:
    		if cur.val == val:
    			pre.next = cur.next
    		else:
    			pre = cur
    		cur = cur.next
    	return dummy.next




    		









