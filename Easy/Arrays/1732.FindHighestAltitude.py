class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix = [gain[0]]
        for i in range(1, len(gain)):
            prefix.append(gain[i]+prefix[i-1])

        max_prefix = max(prefix)
        return 0 if max_prefix <=0 else max_prefix
        
sol = Solution()
print(sol.largestAltitude(gain = [-5,1,5,0,-7]))     