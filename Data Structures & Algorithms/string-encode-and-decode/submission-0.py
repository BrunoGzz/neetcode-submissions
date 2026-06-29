class Solution:

    def encode(self, strs: List[str]) -> str:
        lenght = len(strs)
        encoded_string = str(f"{lenght:03d}")
        for string in strs:
            stringInt = len(string)
            encoded_string += str(f"{stringInt:03d}")
            encoded_string += string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        actualIndex = 3
        decoded_strs = []
        for i in range(int(s[:3])):
            lenghtOfString = int(s[actualIndex:actualIndex+3])
            decoded_strs.append(s[actualIndex+3:actualIndex+3+lenghtOfString])
            actualIndex += 3 + lenghtOfString
        return decoded_strs
