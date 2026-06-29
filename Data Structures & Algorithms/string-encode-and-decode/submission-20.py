class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            if i == 0:
                encoded = strs[i] + "-"
            elif i == len(strs) -1:
                encoded += strs[i] + "-"
            else:
                encoded += strs[i] + "-"

        return encoded

    def decode(self, s: str) -> List[str]:
        encoded = s
        decoded = []
        temp = ""
        for ch in encoded:
            if ch == "-":
                decoded.append(temp)
                temp = ""
            else:
                temp += ch
                

        return decoded
