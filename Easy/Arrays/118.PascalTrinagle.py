from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle list
        triangle = []

        # Iterate through the rows
        for i in range(numRows):
            # Initialize the current row with 1's
            row = [1] * (i + 1)

            # Calculate the elements of the row
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            # Append the row to the triangle
            triangle.append(row)

        # Return the triangle
        return triangle
