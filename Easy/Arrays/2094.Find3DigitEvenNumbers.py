from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_nums = [n for n in range(100, 1000) if n % 2 == 0]  # ✅ List of 3-digit even numbers
        digit_count = Counter(digits)  # ✅ Track occurrences of digits
        result = []  
        
        for num in even_nums:
            new_d = list(map(int, str(num)))  # ✅ Convert number to individual digits
            num_counter = Counter(new_d)  # ✅ Count needed digits
            
            # ✅ Check if we have enough occurrences of each digit
            if all(num_counter[d] <= digit_count[d] for d in num_counter):
                result.append(num)
        
        return result

sol = Solution()
print(sol.findEvenNumbers([2,2,8,8,2]))

