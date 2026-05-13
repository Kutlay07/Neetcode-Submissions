class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sor = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in sor:
                length = 0
                while n + length in sor:
                    length += 1
                longest = max(length,longest)
        return longest
         