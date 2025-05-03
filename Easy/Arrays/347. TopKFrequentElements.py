from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common_element = Counter(nums).most_common(k)
        final_list = [ele[0] for ele in most_common_element]
        return final_list
            
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))