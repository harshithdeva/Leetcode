from typing import List

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {} 
        
        for i, num in enumerate(nums):
            if num in num_map:
                if abs(i - num_map[num]) <= k:
                    return True
            num_map[num] = i 
        
        return False

sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3],k = 2))


                
