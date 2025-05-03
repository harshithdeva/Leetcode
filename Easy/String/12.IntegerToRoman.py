class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples (integer value, Roman numeral)
        roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        # Initialize result string
        roman = ""
        
        # Iterate through the roman_map and subtract values from num
        for value, symbol in roman_map:
            while num >= value:
                roman += symbol
                num -= value
        
        return roman
