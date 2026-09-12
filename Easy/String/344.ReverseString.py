from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) -1
        while i < j:
            t = s[i]
            s[i] = s[j]
            s[j] = t
            i+=1
            j-=1

        return s

# Doesn't work for all cases
# class Solution2:
#     def reverseString(self, s: List[str]) -> None:
#         return s[::-1]

class Solution2:
        def reverseString(self, s: List[str]) -> None:
            return s.reverse()
        




sol = Solution()
print(sol.reverseString(s = ['a','b','c']))

sol = Solution2()
print(sol.reverseString(s = ['a','b','c']))
