"""
https://leetcode.com/problems/permutations-ii
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def helper(self, nums, curPermute, res, seen = set()):
        if(len(nums) == 0):
            res.append(curPermute)
        for idx, c in enumerate(nums):
            newCurPermute = curPermute[:] + [nums[idx]]
            checkCurPermute = tuple(newCurPermute)
            if(checkCurPermute not in seen):
                seen.add(checkCurPermute)
                self.helper(nums[:idx]+nums[idx+1:], newCurPermute, res, seen)
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        seen = set()
        self.helper(nums, [], res, seen)
        return res