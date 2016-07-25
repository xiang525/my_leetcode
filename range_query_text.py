"""
Data Structure: Interval Tree
"""
class Node(object):
    def __init__(self,start,end):
        self.start = start; self.end = end
        self.left = None; self.right = None
    
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def buildTree(nums,left,right):
            if left > right: return None
            if left == right:
                n = Node(left,right)                
                return n
            mid = (left+right)/2
            root = Node(left, right)
            root.left = buildTree(nums,left, mid)
            root.right = buildTree(nums,mid+1,right)            
            return root
        self.root = buildTree(nums,0,len(nums)-1)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def helper(root,i,val):
            if root.start == root.end:
                root.sums = val
                return val
            mid = (root.start+root.end)/2
            if i <= mid:
                helper(root.left,i,val)
            else:
                helper(root.right,i,val)
            root.sums = root.left.sums + root.right.sums
            return root.sums
        return helper(self.root,i,val)


    def query(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(root,i,j):
            if root.start == i and root.end == j: return True
            mid = (root.start + root.end)/2
            if j <= mid:
                return helper(root.left,i,j)
            elif i >= mid+1:
                return helper(root.right,i,j)
            else:
                return helper(root.left,i,mid) + helper(root.right,mid+1,j)
        return helper(self.root,i,j)



