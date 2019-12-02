# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, low, high, nums, root = None):
        mid = (low+high)/2
        node = TreeNode(nums[mid])
        if(node.val > root.val):
            root.right = node
        else:
            root.left = node
        if(low != mid):
            self.helper(low, mid-1, nums, node)
            self.helper(mid+1, high, nums, node)
        elif(low == mid and high != low):
            node.right = TreeNode(nums[high])
        return node
            
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if(not nums):
            return None
        return self.helper(0, len(nums)-1, nums, TreeNode(0))
        