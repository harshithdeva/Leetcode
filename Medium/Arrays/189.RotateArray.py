# Approach 1
def rotate(nums, k):
    k = k % len(nums)
    dupnums = [0] * len(nums)
    for i in range(len(nums)):
        dupnums[(i + k) % len(nums)] = nums[i]

    nums[:] = dupnums # copy dupnums to nums
    return nums


# Approch 2
def rotate(nums, k):
    for i in range(k % len(nums)):
        nums.insert(0, nums.pop())


# Google Interview Question
