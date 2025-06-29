class Solution:
    def is_within_int32_range(self, num: int) -> bool:
        return -2**31 <= num <= 2**31 - 1

    
    def reverse(self, x: int) -> int:
        str_int = str(x)
        str_int = str_int[::-1]
        if "-" in str_int:
            str_int = str_int.replace("-","")
            str_int = "-"+str_int
        new_x = int(str_int)
        if self.is_within_int32_range(new_x):
            return new_x
        return 0

sol = Solution()
print(sol.reverse(-321))        