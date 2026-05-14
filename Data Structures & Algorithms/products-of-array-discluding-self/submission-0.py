class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []

        for k in range(len(nums)): # k is the index of the current element to exclude
            current_product = 1
            for l in range(len(nums)): # l iterates through all elements
                if k != l: # if l is not the index of the current element to exclude
                    current_product *= nums[l]
            ans.append(current_product)

        return ans