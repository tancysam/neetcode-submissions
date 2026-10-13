class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return []
        encoded = "-".join(strs)
        return encoded
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        decoded = s.split("-")
        return decoded
