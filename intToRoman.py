"""
https://leetcode.com/problems/integer-to-roman/submissions/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = {
          'I': 1,
          'IV': 4,
          'V': 5,
          'IX': 9,
          'X': 10,
          'XL': 40,
          'L': 50,
          'XC': 90,
          'C': 100,
          'CD': 400,
          'D': 500,
          'CM': 900,
          'M': 1000
        }
        res = ""
        # seems this line is super slow, should have convert it to list first. But too lazy.
        table2 = sorted(table, key=lambda x: table[x], reverse=True)
        for key in table2:
          r = num%table[key]
          q = num/table[key]
          if(q > 0):
            adds = q if key in ["M", "C", "X", "I"] else 1
            num -= table[key] * adds
            res += key * adds
          if(num == 0):
            break
        return res
            