# Using 2 Pointers
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s2 = list(s)
        num = len(s2)
        left = 0
        right = num -1
        while left < right:
            if (s[left].isalpha()) and (s[right].isalpha()):
                s2[right] = s[left]
                s2[left] = s[right]
                left +=1
                right -= 1
            if (not s[left].isalpha()):
                left += 1
            if (not s[right].isalpha()):
                right -= 1
        return "".join(s2)

            

sol = Solution()
print(sol.reverseOnlyLetters("a-bC-dEf-ghIj")) 