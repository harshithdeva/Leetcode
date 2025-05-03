from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_val = max(candies)  
        output_list = [(candy + extraCandies) >= maximum_val for candy in candies] 
        return output_list

# Testing
sol = Solution()
output = sol.kidsWithCandies([2, 3, 5, 1, 3], 3)
print(output) 
            

