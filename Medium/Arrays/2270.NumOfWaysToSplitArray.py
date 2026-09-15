from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])

        ans = 0
        for j in range(len(nums)-1):
            left = prefix[j]
            right = prefix[-1] + prefix[j]
            if left >= right:
                ans +=1

        return ans        

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans

# Need to review