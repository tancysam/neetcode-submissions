class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        num_track = ""
        for string in strs:
            num_track += len(string)
            encoded += string

        encoded = num_track + "-" + encoded
        print(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []

        separator_index = encoded.index("-")
        encoded = s[separator_index+1:]
        num_track = s[0:separator_index].split()

        i = 0

        for num in num_track:
            decoded.append(encoded[i:num-1])
            i += num 

        return decoded

