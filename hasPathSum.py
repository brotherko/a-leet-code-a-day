# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, acc, sum):
        if(not root):
            return False
        if(root.left == None and root.right == None):
            return (acc+root.val) == sum
        else:
            return self.helper(root.left, acc+root.val, sum) or self.helper(root.right, acc+root.val, sum)
            
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(not root):
            return False
        return self.helper(root, 0, sum)