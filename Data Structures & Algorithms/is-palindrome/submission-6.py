class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower().replace(" ", "")
        s2 = ""
        for char in s1:
            if char.isalnum():
                s2 += char
        
        return s2 == s2[::-1]