class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = []
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                final_str.append(word1[i])
                i += 1
            if j < len(word2):
                final_str.append(word2[j])
                j += 1

        return "".join(final_str)

sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"

            

