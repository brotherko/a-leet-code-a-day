"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):

    def helperRecursive(self, nums, low, high, target):
        plus = (high-low)/2
        mid = low + plus
        
        if(target > nums[mid] and plus != 0):
            return self.helperRecursive(nums, mid, high, target)
        elif(target < nums[mid] and plus != 0):
            return self.helperRecursive(nums, low, mid, target)
        else:
            i = 0
            j = len(nums) - 1
            first = last = -1
            while((first == -1 or last == -1) and i <= j):
              if(nums[i] == target):
                first = i
              else:
                i += 1
              if(nums[j] == target):
                last = j
              else: 
                j -= 1
            return [first, last]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums) == 0):
            return [-1,-1]
        # return self.helperRecursive(nums, 0, len(nums)-1, target)
        low = 0
        high = len(nums)-1
        first = last = -1
        while(True):      
            plus = (high-low)/2
            mid = low + plus
            if(target > nums[mid] and plus != 0):
                low = mid
            elif(target < nums[mid] and plus != 0):
                high = mid
            else:
                while(low <= high):
                  if(nums[low] == target and first == -1):
                    first = low
                  else:
                    low += 1
                  if(nums[high] == target and last == -1):
                    last = high
                  else:
                    high -= 1
                break
        return [first, last]