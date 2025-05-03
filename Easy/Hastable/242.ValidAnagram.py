class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper_1 = {}
        for letter in s:
            if letter in mapper_1:
                mapper_1[letter] += 1
            else:
                mapper_1.update({letter:1})
        mapper_2 = {}
        for letter in t:
                if letter in mapper_2:
                    mapper_2[letter] += 1
                else:
                    mapper_2.update({letter:1})
        if mapper_1 == mapper_2:
            return True
        return False