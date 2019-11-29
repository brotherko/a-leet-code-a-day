"""
https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def helper(self, nums, curPermute, res):
        if(len(nums) == 0):
            res.append(curPermute)
        for idx, c in enumerate(nums):
            self.helper(nums[:idx]+nums[idx+1:], curPermute[:] + [nums[idx]], res)
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, [], res)
        return res
        