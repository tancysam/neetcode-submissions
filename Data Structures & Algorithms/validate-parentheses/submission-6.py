class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False

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
                

