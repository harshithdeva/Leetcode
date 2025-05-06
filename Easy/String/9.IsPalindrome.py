class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome_str = str(x)
        reverse_palindrome_str = palindrome_str[::-1]
        return (palindrome_str == reverse_palindrome_str)