class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArray = sorted(nums1 + nums2)
        n = len(sortedArray)

        if n % 2 != 0:
            return sortedArray[n//2]
        else:
            mid = sortedArray[n//2-1] + sortedArray[n//2]
            return mid / 2