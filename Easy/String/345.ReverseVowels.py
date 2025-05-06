from typing import List

class Solution:
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    def extract_vowels_from_str(self, s:str) -> List:
        list_str = list(s)
        vowels_list = []
        for s in list_str:
            if s in self.vowels:
                vowels_list.append(s)
        vowels_list.reverse()
        return vowels_list

    def reverseVowels(self, s: str) -> str:
        vowels_list = self.extract_vowels_from_str(s)
        vowels_list_counter = 0
        list_str = list(s)
        for i,s in enumerate(list_str):
            if s in self.vowels:
                list_str[i] = vowels_list[vowels_list_counter]
                vowels_list_counter += 1
        final_str = ""
        for letter in list_str:
            final_str += letter
        return final_str
    
sol = Solution()
print(sol.reverseVowels("IceCreAm"))