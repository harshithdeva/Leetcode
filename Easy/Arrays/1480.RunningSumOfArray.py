from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[i-1])

        return  prefix
        