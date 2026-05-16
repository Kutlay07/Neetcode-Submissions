class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        curr = 0
        total = 0
        prefixSum[0] = 1
        for num in nums:
            curr += num
            
            total += prefixSum[curr-k]

            prefixSum[curr] += 1
        return total