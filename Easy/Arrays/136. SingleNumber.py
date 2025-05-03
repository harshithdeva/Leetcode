from typing import List

def singleNumber(nums: List[int]) -> int:
        for n in nums:
            count = nums.count(n)
            if count == 1:
                ele = n
                break
        
        return ele