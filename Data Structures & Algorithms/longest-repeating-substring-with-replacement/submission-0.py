class Solution:
        
    def characterReplacement(self, s: str, k: int):
        
        left = 0
        trackChar = {}
        maxCharFreq = 0

        largestWin = 0

        for i,ch in enumerate(s):
            trackChar.setdefault(ch, 0)
            trackChar[ch] += 1
            winLength = i-left+1
            maxCharFreq = max(trackChar.values())
            maxReplace = winLength - maxCharFreq
            
            while maxReplace > k:
                trackChar[s[left]] -= 1
                left += 1
                maxCharFreq = max(trackChar.values())
                winLength = i-left+1
                maxReplace = winLength - maxCharFreq
            
            largestWin = max(winLength, largestWin)
        
        return largestWin






            
            



    