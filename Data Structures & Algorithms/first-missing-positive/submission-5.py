class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+2):
            if i > 0 and i not in nums:
                return i
                break