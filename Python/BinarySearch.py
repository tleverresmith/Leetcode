# Problem 704

# Thought Process
# Dictionary seems very intelligent here
# Itemize the item into a dictionary, key is the item and the value is the index
# Quick "is in" check for the false values

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        solutionDict = {}
        i = 0
        for num in nums:
            solutionDict[num] = i
            i += 1

        return solutionDict.get(target, -1)
