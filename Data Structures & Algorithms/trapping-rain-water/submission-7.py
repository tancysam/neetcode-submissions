class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []

        pre_max = height[0]
        suf_max = height[len(height)-1]

        for h in height:
            pre.append(pre_max)
            if pre_max < h:
                pre_max = h
        
        for h in height[::-1]:
            suf.append(suf_max)
            if suf_max < h:
                suf_max = h

        suf = suf[::-1]
        print(pre,suf)
        total = 0

        for i in range(len(height)):
            total += min(pre[i],suf[i]) - height[i]
        
        return total