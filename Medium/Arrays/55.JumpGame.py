from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Tracks the farthest index we can reach
        
        for i in range(len(nums)):
            if i > farthest:  # If we reach an index we can't jump to, return False
                return False
            farthest = max(farthest, i + nums[i])  # Update farthest reachable index
            
        return True  # If we finish the loop, we can reach the last index
    
sol = Solution()
print(sol.canJump([2,3,1,1,4]))