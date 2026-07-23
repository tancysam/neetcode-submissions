class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sHash = {}
        tHash = {}

        for i in range(len(s)):
            sHash.setdefault(s[i],0)
            sHash[s[i]] += 1
            tHash.setdefault(t[i],0)
            tHash[t[i]] += 1
        
        return sHash == tHash



        