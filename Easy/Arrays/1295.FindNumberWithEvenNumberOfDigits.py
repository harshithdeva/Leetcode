from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        new_nums = [str(num) for num in nums]
        counter = 0
        for n in new_nums:
            if len(n)% 2 == 0:
                counter += 1
        return counter

sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]))