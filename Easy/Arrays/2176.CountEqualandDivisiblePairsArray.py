from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        i = 0
        counter =0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i*j) %k == 0:
                    counter += 1
        
        return counter

sol = Solution()
print(sol.countPairs([3,1,2,2,2,1,3],2))