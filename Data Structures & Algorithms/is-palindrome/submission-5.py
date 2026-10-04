class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(filter(str.isalnum, s)).lower()
        r = len(text) - 1

        for l in text:
            if l == text[r]:
                r -= 1
            else:
                return False
        return True