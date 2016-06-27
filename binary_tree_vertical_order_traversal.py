
"""
论坛的解法, 很耗空间
"""

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                cols[i].append(node.val)
                queue.append((node.left, i - 1))# root index 为i时， left is i-1 and right is i+1
                queue.append((node.right, i + 1))
        return [cols[i] for i in sorted(cols)] #按col输出