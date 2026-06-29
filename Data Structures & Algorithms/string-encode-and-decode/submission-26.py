class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        num_track = ""
        for string in strs:
            num_track += str(len(string)) + "#"
            encoded += string 

        encoded = num_track + "-" + encoded


        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []

        separator_index = s.index("-")
        encoded = s[separator_index+1:]
        num_track = s[0:separator_index].split("#")[:-1]


        i = 0
        for j in range(len(num_track)):
            decoded.append(encoded[i:i+int(num_track[j])]) # Previous error: did not add i to end, thought length could only be one digit
            i += int(num_track[j])


        return decoded

