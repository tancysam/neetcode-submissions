class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        maxL = 0
        currL = 0
        prev = 0

        for ch in s:
            if ch not in charSet:
                charSet.add(ch)
                currL += 1
                
            else:
                while ch in charSet:
                    print(charSet,maxL)
                    charSet.remove(s[prev])
                    currL -= 1
                    prev += 1
                charSet.add(ch)
                currL += 1

            maxL = max(currL,maxL)

        
        return maxL

            

