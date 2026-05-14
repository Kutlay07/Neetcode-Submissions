class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        sorted_items = sorted(freq.items(),key=lambda item: item[1],reverse=True)

        for i in range(min(k,len(sorted_items))):
            res.append(sorted_items[i][0])
        return res