from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapper = {}  # Dictionary to store counts
        
        for n in nums:
            if n in mapper:
                mapper[n] += 1  
            else:
                mapper[n] = 1
        
        for val in mapper.values(): 
            if val >= 2:
                return True
        
        return False