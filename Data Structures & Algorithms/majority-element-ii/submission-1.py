class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []

        for i in nums:
            count[i] = count.get(i,0) + 1

        for key,value in count.items():
            if value > len(nums) / 3:
                res.append(key)
        return res