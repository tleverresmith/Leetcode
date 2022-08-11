class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                nums.insert(j, nums.pop(i))
                j -= 1
            else:
                i += 1


x = Solution
x.moveZeroes(x, [0, 0, 1])
