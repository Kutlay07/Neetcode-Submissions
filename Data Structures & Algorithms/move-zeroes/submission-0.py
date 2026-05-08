class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        kk = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[kk],nums[i] = nums[i],nums[kk]
                kk += 1
        return nums