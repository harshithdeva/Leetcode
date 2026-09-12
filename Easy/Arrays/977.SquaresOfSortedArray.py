from typing import List

# Easy Way
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i] = nums[i] * nums[i]

        return sorted(nums)

# Using 2 Pointers
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        nums2 = []

        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                nums2.append(nums[j] ** 2)
                j -= 1
            else:
                nums2.append(nums[i] ** 2)
                i += 1

        return nums2[::-1]


        

s = Solution()
print(s.sortedSquares(nums=[-7,-3,2,3,11]))

s = Solution2()
print(s.sortedSquares(nums=[-7,-3,2,3,11]))