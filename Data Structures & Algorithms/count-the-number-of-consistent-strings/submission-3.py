class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = {}
        length = len(words)

        for i in allowed:
            al[i] = al.get(i,0) + 1

        for i in words:
            word_count = {}
            for word in i:
                word_count[word] = word_count.get(word,0) + 1

            for key,value in word_count.items():
                if key not in al:
                    length -= 1
                    break
                    
        return length