# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, stack, result, node, depth):
        stack.append([node, depth])
        if(depth < len(result)):
            result[depth].append(node.val)
        else:
            result.append([node.val])
            
    def levelOrder(self, root):
        """(((
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        stack = [[root, 0]]
        result = [[root.val]]
        while(stack):
            root, depth = stack.pop(0)
            if(root.left):
                self.helper(stack, result, root.left, depth+1)
            if(root.right):
                self.helper(stack, result, root.right, depth+1)
        return result