"""
不是最优解用了extra space O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ans = []
        while head:
            ans += head.val,
            head = head.next
        return ans == ans[::-1]


"""
论坛里的写法， O(n) + O(1) space
Solution: Reversed second half == first half?
Phase 1: find the middle.
Phase 2: Reverse the second half 
Phase 3: Compare the reversed second half with the first half.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
    # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
    # reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
    # compare the first and second half nodes
        while prev: # while node and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True



        