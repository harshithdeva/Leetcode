from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 
        ans = 0
        curr = 1
        if k <=1:
            return 0
        for right in range(len(nums)):
            curr = curr * nums[right]
            while curr >= k:
                curr = curr/nums[left]
                left += 1
            ans = right - left + 1

        return ans


## To be re-reviewed later