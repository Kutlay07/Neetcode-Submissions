class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy_list = []
        dict = {}

        for i in range(len(strs)):
            string = strs[i]
            sorted_string = sorted(string)
            key_string = "".join(sorted_string)
            if key_string not in dict:
                dict[key_string] = []
            dict[key_string].append(string)

        output = []
        for i in dict:
            output.append(dict[i])
        return output