from typing import List

class Solution:
    
    def dynamic(self,num_list):
        prev1, prev2 = 0, 0  # Stores dp[i-1] and dp[i-2]
        
        for num in num_list:
            new_rob = max(prev1, prev2 + num)  # Apply DP formula
            prev2 = prev1  # Move forward
            prev1 = new_rob  # Update max robbed amount
        
        return prev1  # Final max amount robbed
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        case1 = self.dynamic(nums[1::])
        case2 = self.dynamic(nums[:-1:])

        return max(case1,case2)



sol = Solution()
print(sol.rob([1,2,3]))






