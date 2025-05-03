from typing import List

def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    for i in range(0,k):
        min_ele = min(nums)
        min_ind = nums.index(min_ele)
        min_ele = min_ele * multiplier
        nums.insert(min_ind,min_ele)
        nums.pop(min_ind+1)
    
    print(nums)

getFinalState(nums=[2,1,3,5,6],k=5,multiplier= 2)