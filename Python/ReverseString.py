class Solution:
    def reverseString(self, s: list[str]) -> None:
        l = 0  # Left most index
        r = len(s) - 1  # Right most index

        while l < r:  # Go until the left index passes the right index, or they collide.
            if s[l] != s[r]:  # If the two elements do not match, swap them around
                lv = s[l]
                rv = s[r]
                s[l] = rv
                s[r] = lv

            l += 1
            r -= 1


Solution.reverseString(Solution, ["H", "a", "n", "n", "a", "h"])
