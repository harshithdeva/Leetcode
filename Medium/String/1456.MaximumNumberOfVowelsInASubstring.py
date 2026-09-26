class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr = 0
        max_len = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        max_len = curr
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr+= 1
            if s[i-k] in vowels:
                curr-= 1
            max_len = max(max_len,curr)

        return max_len


       


sol = Solution()
print(sol.maxVowels(s = "abciiidef", k = 3))
        