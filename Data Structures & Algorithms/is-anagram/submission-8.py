class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sSet = set(s)
        tSet = set(t)

        return sSet == tSet and len(s) == len(t)