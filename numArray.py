class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if(not nums):
            return None
        self.memo = [nums[0]]
        i = 1
        while(i < len(nums)):
            self.memo.append(nums[i]+self.memo[i-1])
            i += 1
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.memo[j]-(self.memo[i-1] if i-1>=0 else 0)
        
