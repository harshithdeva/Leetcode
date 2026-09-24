class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_len = len(word)
        if ch in word:
            ch_ind = word.index(ch)
            part_word = word[0:ch_ind+1]
            part_word2 = word[ch_ind+1:ch_len]
            part_word = part_word[::-1]
            return part_word+part_word2
        return word

sol = Solution()
print(sol.reversePrefix(word = "xyxzxe", ch = "z"))