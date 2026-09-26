class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        curr = 0
        max_len = float('-inf')
        for right in range(len(s)):
            curr += abs(ord(s[right])-ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_len = max(max_len, right - left + 1)
            

        return 1 if max_len == float('-inf') else max_len


sol = Solution()
print(sol.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))