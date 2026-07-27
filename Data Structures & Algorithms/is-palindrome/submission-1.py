class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = "".join(char for char in s if char.isalnum()).lower()
        r = len(s) - 1
        
        while l < r:
            print(l,r)
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        return True