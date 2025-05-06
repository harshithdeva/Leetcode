from typing import List

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # index to write the compressed characters
        read = 0   # index to read through the input list

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # If count > 1, write the count as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write