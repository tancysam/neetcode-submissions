class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = "-".join(strs)
        return encoded
    def decode(self, s: str) -> List[str]:

        decoded = s.split("-")
        return decoded
