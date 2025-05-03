class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If `s` is empty, it's a subsequence of any string.
        if not s:
            return True

        i, j = 0, 0

        # Iterate through `t` while checking `s`
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1

        # Check if all characters in `s` have been matched
        return i == len(s)
    
    
sol = Solution()
print(sol.isSubsequence(s = "abc", t = "ahbgdc"))

sol1 = Solution()
print(sol1.isSubsequence(s = "axc", t = "ahbgdc"))