from PalindromeNumber import Solution


def tests(testDict: dict):
    for test in testDict:
        assert Solution.isPalindrome(
            Solution, test) == testDict[test], f"{test} did not pass"


if __name__ == "__main__":
    testDict = {
        -1: False,
        1: True,
        11: True,
        1221: True,
        -1221: False,
        121: True,
        12121: True,
        1223221: True
    }

    tests(testDict)
    print("Tests Passed")
