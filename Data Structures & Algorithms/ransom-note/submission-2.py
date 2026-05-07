class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomFreq = {}
        magazFreq = {}

        for i in ransomNote:
            ransomFreq[i] = ransomFreq.get(i,0) + 1

        for i in magazine:
            magazFreq[i] = magazFreq.get(i,0) + 1

        for key,value in ransomFreq.items():
            if key not in magazFreq or ransomFreq[key] > magazFreq[key]:
                return False

        return True