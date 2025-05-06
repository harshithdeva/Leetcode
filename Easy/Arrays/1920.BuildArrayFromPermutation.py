from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        original_len = len(nums)
        new_list = [nums[nums[i]] for i in range(original_len)]
        return new_list

sol = Solution()
print(sol.buildArray([0,2,1,5,3,4]))