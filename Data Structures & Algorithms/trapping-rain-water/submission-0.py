class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        res = 0

        current_max = height[0]
        for i in range(len(height)):
            current_max = max(current_max, height[i])
            leftMax.append(current_max)


        current_max = height[-1]
        for i in height[::-1]:
            current_max = max(current_max,i)
            rightMax.append(current_max)

        rightMax.reverse()

        for i in range(len(height)):
            res += min(leftMax[i],rightMax[i]) - height[i]

        return res