import statistics
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = nums1 + nums2
        merged_nums = sorted(merged_nums)
        return statistics.median(merged_nums)
