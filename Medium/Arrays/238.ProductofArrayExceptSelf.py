import math

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Step 1: Compute prefix product (product of elements before the current one)
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Step 2: Compute suffix product (product of elements after the current one)
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  

# ### **Step-by-Step Explanation**
# #### 🔹 **Step 1: Initialize Output Array**
# - Create an array `output` of size `n` filled with `1`. This will store the final result.

# #### 🔹 **Step 2: Compute Prefix Product**
# - Traverse **forward** (`left to right`) and store the **product of all elements before the current one**.
# - Example:
#   - `output[0]` remains `1` (since nothing is before it).
#   - `output[1] = 1 * nums[0]` → `output[1] = 1 * 1 = 1`
#   - `output[2] = 1 * 2` → `output[2] = 2`
#   - `output[3] = 2 * 3` → `output[3] = 6`

# #### 🔹 **Step 3: Compute Suffix Product**
# - Traverse **backward** (`right to left`) and store the **product of all elements after the current one**.
# - Example:
#   - `output[3]` remains `6` (since nothing is after it) suffix = 1
#   - `output[2] *= nums[3]` → `output[2] = 2 * 4 = 8` suffix = 4 (1*3)
#   - `output[1] *= nums[2]` → `output[1] = 1 * 3 = 12` suffix = 12 (4*3)
#   - `output[0] *= nums[1]` → `output[0] = 1 * 2 = 24` suffix = 24 (12*2)

# ---


# Inefficient for Large Inputs
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod_nums = []
#         final_list = []
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums)):
#                 if j==i:
#                     continue
#                 product = 1
#                 prod_nums.append(product*nums[j])
                
#             final_list.append(math.prod(prod_nums))
#             prod_nums = []
#         return final_list

