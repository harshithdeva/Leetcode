from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_value = 0
        for num in nums:
            prefix_sum += num
            min_value = min(min_value, prefix_sum)
        return 1 - min_value

        
        