class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Initialize res with a very large number to ensure the first comparison finds a smaller value
        res = float('inf')

        # Iterate through all possible starting indices for a subarray of length k
        # The loop should go up to len(nums) - k, inclusive, so that the last subarray ends at len(nums)-1
        for i in range(len(nums) - k + 1):
            # For a sorted subarray of length k (nums[i:i+k]), the minimum is nums[i] and the maximum is nums[i+k-1]
            current_diff = nums[i + k - 1] - nums[i]
            res = min(res, current_diff)

        return res