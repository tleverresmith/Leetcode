from BinarySearch import Solution


def tests(testArray: tuple):
    for test in testArray:
        assert Solution.search(
            Solution, test[0], test[1]) == test[2], f"{test[0]}, {test[1]} did not pass"


if __name__ == "__main__":
    testArray = [
        ([1, 2, 3, 4, 5], 4, 3),  # List of Integers, target, index
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 100, -1)

    ]

    tests(testArray)
    print("Tests Passed")
