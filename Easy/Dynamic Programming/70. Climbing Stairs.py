# Dynamic Programming Question, refered online to solve

# Link to solution refered https://www.youtube.com/watch?v=Y0lT9Fck7qI


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n in [0,1,2]:
            return n

        # Initialize the first two steps
        first = 1
        second = 2
        for i in range(3,n+1):
            current = first + second
            first = second
            second = current

        return second