from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg_sum = 0
        sum_1 = 0
        for i in range(0,k):
            sum_1+= nums[i]

        avg_sum = (sum_1/k)

        ans = avg_sum
        for j in range (k, len(nums)):
            sum_1 += (nums[j] - nums[j-k])
            avg_sum = (sum_1 /k)
            ans = max(ans,avg_sum)

        return ans

            

