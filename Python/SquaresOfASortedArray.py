# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        # Initiate a new array to hold the sorted values. Set l(eft) to 0 and r(ight) to the last index of the array
        ansArray = []
        l = 0
        r = len(nums) - 1

        # While the left index is lower than the right index keep it going, otherwise we have sorted the objects in the new array
        while l <= r:

            # Evaluate the elements at index l and r.
            # Square both elements and pop the largest element, inserting it in position 0 of the answer array.
            if nums[l] ** 2 < nums[r] ** 2:
                ansArray.insert(0, nums.pop(r) ** 2)
                r = r - 1
            else:
                ansArray.insert(0, nums.pop(l) ** 2)
                r = r - 1

        return ansArray
