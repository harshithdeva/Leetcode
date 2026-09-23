
# Through 2 Pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = list(s)
        n  = len(s2)
        start = 0
        for i in range (n+1):
            if i == n or s[i] == " ":
                left = start
                right = i - 1
                while left < right:
                    s2[right] = s[left]
                    s2[left] = s[right]
                    left += 1
                    right -= 1
                start = i + 1


        
        s2 =  "".join(s2)
        return s2

# Python Way
class Solution2:
    def reverseWords(self, s: str) -> str:
        return (" ".join(word[::-1] for word in s.split()))

sol = Solution()
print(sol.reverseWords("Mr Ding"))

sol1 = Solution2()
print(sol1.reverseWords("Mr Ding"))

        