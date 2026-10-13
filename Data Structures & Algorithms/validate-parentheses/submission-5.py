class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mp = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[" :
                stack.append(ch)
            else:
                mp_ch = mp[ch]
                temp = stack.pop()
                if temp != mp_ch:
                    return False

        return True
                

