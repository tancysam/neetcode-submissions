class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        child = 0

        g.sort()
        s.sort()
        print(g,s)

        for i in range(len(s)):
            if i < len(g):
                if s[i] >= g[i]:
                    child += 1
            else:
                pass
        
        return child
