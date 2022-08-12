class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # PLANNING

        # First, sort the list
        nums.sort()

        # Store the max length of the array

        for index, value in enumerate(nums):
            if index == len(nums) - 1:
                return value

            if not nums[index] == nums[index - 1] and not nums[index] == nums[index + 1]:
                return value


x = Solution
print(x.singleNumber(x, [4, 1, 2, 1, 2]))
