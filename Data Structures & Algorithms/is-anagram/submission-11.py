class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sHash = {}
        tHash = {}

        for ch in s:
            sHash.setdefault(ch, 0)
            sHash[ch] += 1

        for ch in t:
            tHash.setdefault(ch,0)
            tHash[ch] += 1
        
        if sHash == tHash:
            return True
        else:
            return False