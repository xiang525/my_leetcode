"""
DFS + heap 
O(nlogn + k)
"""

class Solution(object):

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(root, target, heap):
            if root is None:
                return
            dfs(root.left, target, heap)# 这里没有顺序可言，因为heappush会调整为min heap
            heapq.heappush(heap, (abs(root.val - target), root.val))
            dfs(root.right, target, heap)

        heap = []
        dfs(root, target, heap)

        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        return output


"""
inorder travesal O(n)
"""
def closestKValues(self, root, target, k):
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    inorder=self.inorder_traversal(root)
    result=inorder[:k]
    for i in xrange(k,len(inorder)):
        if abs(result[0]-target)>abs(inorder[i]-target):
            result.append(inorder[i])
            result=result[1:]
        else:
            return result
    return result


def inorder_traversal(self,root):
    stack=[]
    res=[]
    #stack.append(root)
    while stack or root:
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            res.append(root.val)
            root=root.right
    return res
