class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            sorted_strs = "".join(sorted(word))
            if sorted_strs not in res:
                res[sorted_strs] = [word]
            elif sorted_strs in res:
                res[sorted_strs].append(word)
        return list(res.values())