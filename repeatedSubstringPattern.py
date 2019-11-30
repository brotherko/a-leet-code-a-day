class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while(i < len(s)):
            if(s[i] == s[0] and len(s)%i == 0 and s == s[0:i]*(len(s)/i)):
                return True
            i += 1
        return False