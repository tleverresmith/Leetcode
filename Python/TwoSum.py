# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# TODO - Document this

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1

        # Find the top index of our search (values less than the target)
        if nums[len(nums) - 1] > target and target > 0:
            while nums[r] > target:
                r = r-1

        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]

            elif nums[l] + nums[r] > target:
                r = r - 1
                l = 0

            else:
                l = l + 1

           # if l + 1 == r:
           #     l = 0
           #     r = r-1


Solution.twoSum(Solution, [0, 0, 3, 4], 0)
