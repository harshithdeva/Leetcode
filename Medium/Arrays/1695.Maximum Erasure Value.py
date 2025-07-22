from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # This will store the maximum sum of a subarray with all unique elements
        ans = 0

        # This keeps track of the current sum of the unique subarray
        current_sum = 0

        # A set to store the elements in the current window (for uniqueness check)
        seen = set()

        # Left pointer for the sliding window
        left = 0

        # Iterate through the array using the right pointer
        for right in range(len(nums)):
            # If we encounter a duplicate element (nums[right] is already in the window)
            while nums[right] in seen:
                # Remove the leftmost element from the sum and the set
                current_sum -= nums[left]
                seen.remove(nums[left])
                # Move the left pointer to the right
                left += 1

            # Add the current element to the set and update the current sum
            seen.add(nums[right])
            current_sum += nums[right]

            # Update the maximum sum found so far
            ans = max(ans, current_sum)

        # Return the maximum sum of a subarray with all unique elements
        return ans
