class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for ch in s:
            # If the last two characters in result are same as current, skip
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                continue
            result.append(ch)

        return ''.join(result)
                