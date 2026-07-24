class Solution:

    def encode(self, strs: List[str]) -> str:
        
        nums = []
        toSend = ""

        for st in strs:
            nums.append(str(len(st))) 
            toSend += st
        nums = ",".join(nums)

        return nums+"<|SplitText|>"+toSend

    def decode(self, s: str) -> List[str]:

        nums, toSend = s.split("<|SplitText|>")

        res = []
        i = 0
        nums = nums.split(",")

        if nums[0] == "":
            return []
        for ch in nums:
            res.append(toSend[i:i+int(ch)])
            i += int(ch)

        
        return res

