class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0

        if target in nums:
            for num in nums:
                if num == target:
                    return i
                else:
                    i += 1

        for num in nums:
            if num > target:
                return i
            else:
                i += 1

        if i == len(nums):
            return i


print(Solution.searchInsert(Solution, [1, 2, 3, 4, 5], 4))
