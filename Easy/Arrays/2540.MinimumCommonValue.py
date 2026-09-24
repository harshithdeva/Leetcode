# 2 Pointer Approach
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = 0
        j = 0
        min_val = float('inf')
        found = False
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] == nums2[j]:
                min_val = min(min_val, nums1[i])
                found = True
                i+=1
                j+=1

            

        return min_val if found else -1




# Brure Force
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        min_arr = list()
        for i in nums1:
            if i in nums2:
                min_arr.append(i)
        if min_arr:
            return min(min_arr)
        return -1
                
