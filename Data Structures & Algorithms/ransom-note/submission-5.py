class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = defaultdict(int)

        for i in magazine:
            seen[i] += 1

        for r in ransomNote:
            if seen[r] > 0:
                seen[r] -= 1
            else:
                return False
        return True