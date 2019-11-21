"""
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def travelLeft(root, res):
            if(root):
                travelLeft(root.left, res)
                travelLeft(root.right, res)
                res.append(root.val)
            else:
                res.append(None)
            return res
        def travelRight(root, res):
            if(root):
                travelRight(root.right, res)
                travelRight(root.left, res)
                res.append(root.val)
            else:
                res.append(None)
            return res
        # print(travelLeft(root))
        def helper(root):
            left = travelLeft(root, [])
            right = travelRight(root, [])
            print(left, right)
            for idx, v in enumerate(left):
                if(left[idx] != right[idx]):
                    return False
            return True
        return helper(root)
        