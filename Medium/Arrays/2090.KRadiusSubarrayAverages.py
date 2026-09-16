from typing import List

# Prefix Sum Approach

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        result = [-1] * n

        if window_size > n:
            return result

        # Build prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # Compute averages
        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            result[i] = total // window_size

        return result


# Brute Force
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        final_arr = []
        n = len(nums)
        for i in range(0,n):
            if i<k:
                final_arr.append(-1)
            elif (n-1-i) < k:
                final_arr.append(-1)
            else:
                avg_arr = []
                avg_arr = nums[i-k:i+k+1]
                sum_arr= sum(avg_arr)
                avg_sum = sum_arr//(2*k+1)
                final_arr.append(avg_sum)
        return final_arr