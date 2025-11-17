from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        alt_len = 0

        # Count evens and odds
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        # Find the longest alternating parity subsequence
        prev = -1
        for num in nums:
            if prev == -1:
                alt_len = 1
                prev = num % 2
            else:
                if num % 2 != prev:
                    alt_len += 1
                    prev = num % 2

        return max(even, odd, alt_len)