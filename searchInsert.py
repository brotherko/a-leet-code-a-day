"""
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

# V1
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        if(len(nums) == 0):
          return 0
        elif(len(nums) == 1):
          return int(target > nums[0])
        else:
          while(True):
            plus = (high-low)/2
            mid = low + plus 
            if(target > nums[mid] and plus != 0):
              low = mid
            elif(target < nums[mid] and plus != 0):
              high = mid
            else:
              break
        
        if(nums[mid] == target):
          return mid
        if(target <= nums[low]):
          return low
        elif(target > nums[low] and target <= nums[high] or target == nums[high]):
          return high
        else:
          return high + 1

#V2
    def searchInsertV2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        if(len(nums) == 0):
          return 0
        elif(len(nums) == 1):
          return int(target > nums[0])
        else:
          while(low < high):
            mid = (low + high)/2
            if(target == nums[mid]):
              return mid
            elif(target < nums[mid]):
              high = mid
            else:
              low = mid+1
        return low
          