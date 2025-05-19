from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = []
        for n in nums1:
            if n in nums2:
                new_list.append(n)
        
        return list(set(new_list))