class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            print xor, i+1, nums[i]
            xor = xor^ (i+1) ^ nums[i]
            #print 'after: ', xor, i+1, nums[i]
        return xor


def constructBST(nums):
    if not nums: return 
    n = len(nums)
    root = TreeNode(nums[n/2])
    root.left = constructBST(nums[:n/2])
    root.right = constructBST(nums[n/2+1:])
    return root




if __name__ == '__main__':
    ins = Solution()
    print ins.missingNumber([0,1,2,3,4,5,6,8,9,10])
    
    