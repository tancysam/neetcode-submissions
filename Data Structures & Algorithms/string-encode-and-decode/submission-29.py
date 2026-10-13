class Solution:

    def encode(self, strs: List[str]) -> str:
        
        nums = ""
        toSend = ""

        for st in strs:
            nums += str(len(st))
            toSend += st
        
        return nums+"<|SplitText|>"+toSend

    def decode(self, s: str) -> List[str]:
        
        nums, toSend = s.split("<|SplitText|>")

        res = []
        i = 0
        for ch in nums:
            res.append(toSend[i:i+int(ch)])
            i += int(ch)

        
        return res

