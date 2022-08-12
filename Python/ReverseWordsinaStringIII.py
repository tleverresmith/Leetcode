# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
#
# Constraints:
#     1 <= s.length <= 5 * 104
#     s contains printable ASCII characters.
#     s does not contain any leading or trailing spaces.
#     There is at least one word in s.
#     All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        # Cast the string to a list
        s = list(s)

        # Pointers used to check our array
        l, r = 0, 1

        # Tracking the final index of the array
        maxLength = len(s) - 1

        endOfList = False

        while s:
            if r > maxLength:
                return ''.join(s)

            while s[r] != ' ' and endOfList == False:
                if r == maxLength:
                    endOfList = True
                else:
                    r = r + 1

            eow = r  # store the end of the word index for use later
            if r != maxLength:
                r = r - 1  # Decrement because we have hit a space

            while l < r:
                s[l], s[r] = s[r], s[l]
                l = l+1
                r = r-1

            l = eow + 1
            r = l + 1


x = Solution
arg = "You like me"
x.reverseWords(x, arg)
