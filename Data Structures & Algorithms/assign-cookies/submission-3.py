class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        i = 0

        while i < len(g) and j <len(s):
            if g[i] <= s[j]:
                i += 1
            j+= 1
        return i