class Solution:

    def encode(self, strs: List[str]) -> str:
        input_list = ""
        for word in strs:
            input_list += str(len(word)) + "#" + word

        return input_list

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1

            word = s[start:start + length]

            result.append(word)

            i = start + length
        return result