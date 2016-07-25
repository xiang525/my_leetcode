"""
线段树的做法
"""
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sums = 0
        self.left = None
        self.right = None


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def buildTree(nums, left, right):
            if left > right:return None
            if left == right:
                n = Node(left, right)
                n.sums = nums[left]
                return n
            mid = (left + right) / 2
            root = Node(left, right)
            root.left = buildTree(nums, left, mid)
            root.right = buildTree(nums, mid+1, right)
            root.sums = root.left.sums + root.right.sums
            return root
        self.root = buildTree(nums, 0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            if root.start == root.end:
                root.sums = val
                return val
            mid = (root.start + root.end) / 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.sums = root.left.sums + root.right.sums
            return root.sums
            
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.sums
            mid = (root.start + root.end) / 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)


    
"""
另一种写法
"""
class Node(object):
    def __init__(self,start,end):
        self.start = start; self.end = end
        self.sums = 0; self.left = None; self.right = None
    
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def buildTree(nums,left,right):
            if left > right: return None
            if left == right:
                n = Node(left,right) # leaves
                n.sums = nums[left]
                return n
            mid = (left+right)/2
            root = Node(left, right)
            root.left = buildTree(nums,left, mid)
            root.right = buildTree(nums,mid+1,right)
            root.sums = root.left.sums + root.right.sums
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


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(root,i,j):
            if root.start == i and root.end == j: return root.sums
            mid = (root.start + root.end)/2
            if j <= mid:
                return helper(root.left,i,j)
            elif i >= mid+1:
                return helper(root.right,i,j)
            else:
                return helper(root.left,i,mid) + helper(root.right,mid+1,j)
        return helper(self.root,i,j)
        

