class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative number can't be palindrome
        reverse = int(str(x)[::-1])
        return reverse == x
