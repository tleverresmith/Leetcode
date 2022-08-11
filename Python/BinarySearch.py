# Problem 704 - Binary Search
#
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution:

    def search(self, nums: list[int], target: int) -> int:
        low = 0  # Array starts at 0 always
        high = len(nums) - 1  # To avoid out of range errors

        # While low is less than or equal to high, iterate through the list to try and find the target value
        while low <= high:

            # Take the list and find the middle point
            mid = (low + high) // 2

            # If the target is higher than the median index, set the new low to mid + 1.
            # We already checked the value at mid so increment past it and test the remaining array
            if target > nums[mid]:
                low = mid + 1

            # If the target is lower than the median index, set the new high to mid - 1
            # We already checked the value at mid so decrement our top value past it and test the remaining array
            elif target < nums[mid]:
                high = mid - 1

            # Implicitly, if the target is not greater or less than the index it is equal to the index so return it
            else:
                return mid

        # If the low increments past high that means we checked all possible positions and came up blank, therefore return -1
        return -1


class alt_Solution:
    # This was my first pass at the problem and is in O(1) time rather than O(log n) time.
    # Although faster due to the lack of collisions in the data set this is not the true intent of the excercise (Binary search)
    def search(self, nums: list[int], target: int) -> int:

        solutionDict = {}
        i = 0
        for num in nums:
            solutionDict[num] = i
            i += 1

        return solutionDict.get(target, -1)


x = Solution
print(x.search(x, [-1, 0, 3, 5, 9, 12], 19))
