# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if it is a negative number, if so, return false automatically
        if 0 > x:
            return False

        # Map the int to an array
        numberArray = list(map(int, str(x)))

        # If it is a single digit return False
        if len(numberArray) == 1:
            return True

        i = 0
        ni = -1
        returnValue = True

        while i < len(numberArray) / 2:
            if numberArray[i] != numberArray[ni]:
                returnValue = False
            i += 1
            ni = ni - 1

        return returnValue
