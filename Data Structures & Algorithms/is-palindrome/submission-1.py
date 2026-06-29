class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        i = 0
        
        while i < len(s)//2:
            if s[i] != s[-i-1]:
                return False
            i += 1
        return True