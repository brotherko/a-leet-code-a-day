"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
"""
class Solution(object):
    def helper(self, digits, s, result):
        if(len(digits) == 0):
            if(s != ""): result.append(s)
            return
        
        pads = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for idx, v in enumerate(pads[int(digits[0])-2]):
            self.helper(digits[1:], s+v, result)
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        self.helper(digits, "", result)
        return result
            
print(Solution().letterCombinations("23"))