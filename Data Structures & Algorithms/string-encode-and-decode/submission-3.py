class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            word_len = int(s[i:j])

            word = s[j + 1: j + 1 + word_len]
            ans.append(word)
            
            i = j + 1 + word_len
        return ans