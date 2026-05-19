class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashTable = {}

        for i in nums:
            hashTable[i] = hashTable.get(i,0) + 1

        for i in range(1,len(nums)+2):
            if i > 0 and i not in nums:
                return i
                break