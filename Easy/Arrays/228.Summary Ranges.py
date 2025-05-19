from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges_list = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return list(map(str,nums))
        result = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                result.append(f"{start}->{nums[i - 1]}" if start != nums[i - 1] else str(start))
                start = nums[i]
        result.append(f"{start}->{nums[-1]}" if start != nums[-1] else str(start))
        return result

sol = Solution()
print(sol.summaryRanges(nums= [0,1,2,4,5,7]))