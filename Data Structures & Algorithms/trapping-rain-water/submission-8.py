class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []

        pre_max = height[0]
        suf_max = height[len(height)-1]

        for h in height:
            pre_max = max(pre_max, h)
            pre.append(pre_max)
        
        for h in height[::-1]:
            suf_max = max(suf_max,h)
            suf.append(suf_max)

        suf = suf[::-1]
        total = 0

        for i in range(len(height)):
            total += min(pre[i],suf[i]) - height[i]
        
        return total