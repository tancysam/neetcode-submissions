class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for string in strs:
            parts.append(str(len(string)))
            parts.append("#")
            parts.append(string)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            decoded.append(s[start:end])
            i = end

        return decoded