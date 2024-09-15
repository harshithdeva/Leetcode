def majorityElement(nums):
        lookup = {}
        for i in nums:
            if not lookup.get(i):
                lookup.update({i:1})
            else:
                 temp = lookup.get(i)
                 lookup.update({i:temp+1})
        if not lookup:
            return None
        else:
            max_key = max(lookup, key=lookup.get)
            return max_key

print(majorityElement([2,2,1,1,1,2,2]))

    # Solved on my own
# More Better Solutions

from collections import Counter

def majorityElement1(self, nums) -> int:
        counter = Counter(nums)
        for key in counter:
            if counter[key] > len(nums)//2:
                return key
            

def majorityElement2(self, nums) -> int:
        nums.sort()
        mid = len(nums)//2
        return nums[mid]
