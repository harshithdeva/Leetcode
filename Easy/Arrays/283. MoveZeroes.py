from typing import List

def moveZeroes(nums: List[int]) -> None:
        num_zeroes = nums.count(0)
        if num_zeroes > 0:
            for i in range(0,num_zeroes):
                index = nums.index(0)
                nums.pop(index)
                nums.append(0)
        return nums