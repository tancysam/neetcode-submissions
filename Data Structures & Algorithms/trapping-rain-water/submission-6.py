class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []

        pre_max = 0
        suf_max = 0

        for h in height:
            pre.append(pre_max)
            if pre_max < h:
                pre_max = h
        
        for h in height[::-1]:
            suf.append(suf_max)
            if suf_max < h:
                suf_max = h

        total = 0

        for i in range(len(height)):
            total += max((min(pre[i],suf[i]) - height[i]),0)
        
        return total