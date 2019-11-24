"""
https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        l = map(lambda x: len(x), strs) if len(strs) > 0 else [0]
        prefix = ""
        while(i < min(l)):
          j = 0
          while(j < len(strs)):
            if(strs[0][i] != strs[j][i]):
              return prefix
            elif(j == len(strs)-1):
                prefix += strs[0][i]
            j += 1
          i += 1
        return prefix
# print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix([]))