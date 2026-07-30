class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Set = {}

        for ch in s1:
            s1Set.setdefault(ch, 0)
            s1Set[ch] += 1
        
        window = {}
        windowLen = 0
        isPerm = False

        l = 0

        for i,r in enumerate(s2):
            window.setdefault(r,0)
            window[r] += 1
            windowLen += 1
            if windowLen < len(s1):
                pass
            else:
                print(window,s1Set)
                if window == s1Set:
                    isPerm = True
                else:
                    window[s2[l]] -= 1
                    if window[s2[l]] == 0:
                        window.pop(s2[l])
                    l += 1
                    windowLen -= 1
        return isPerm






