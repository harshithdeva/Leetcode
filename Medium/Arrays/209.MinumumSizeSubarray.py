# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Looked up solution

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                min_len = min(min_len, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
        

        

sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))