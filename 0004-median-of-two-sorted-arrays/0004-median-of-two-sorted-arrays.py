class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = sorted(nums1 + nums2)

        if len(newarr) % 2 == 0:
            m = (newarr[len(newarr)//2 - 1] + newarr[len(newarr)//2]) / 2
        else:
            m = newarr[len(newarr)//2]

        return m