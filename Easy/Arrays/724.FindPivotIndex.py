class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i]+prefix[-1])

        print(prefix)
        
        left_section = 0
        right_section = 0
        for j in range(len(nums)-1):
            left_section = prefix[j]
            print(f"Left:{left_section}")
            right_section = prefix[-1] - prefix[j+1]
            print(f"Right:{right_section}")
            if left_section == right_section:
                return j
        return -1

sol = Solution()
print(sol.pivotIndex([2,1,-1]))

