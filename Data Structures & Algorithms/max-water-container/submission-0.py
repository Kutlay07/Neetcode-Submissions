class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0

        while l<r:
            curr_area = min(height[l],height[r]) * (r-l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            res = max(res,curr_area)
        return res