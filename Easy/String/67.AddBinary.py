class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a,2)
        num_b = int(b,2)

        num_sum = num_a + num_b
        bin_num_sum = str(bin(num_sum))[2:]

        return bin_num_sum