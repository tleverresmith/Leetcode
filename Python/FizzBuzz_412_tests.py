from FizzBuzz_412 import Solution


def tests():
    result = Solution.fizzBuzz(3)
    assert Solution.fizzBuzz(
        3) == ['1', '2', 'Fizz'], f"3 did not pass. Result {result}"

    result = Solution.fizzBuzz(10)
    assert Solution.fizzBuzz(10) == [
        '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'], f"10 did not pass. Result {result}"

    result = Solution.fizzBuzz(15)
    assert Solution.fizzBuzz(15) == [
        '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'], f"15 did not pass. Result {result}"

    result = Solution.fizzBuzz(104)
    assert Solution.fizzBuzz(104) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53',
                                      'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz', '101', 'Fizz', '103', '104'], f"15 did not pass. Result {result}"


if __name__ == "__main__":
    tests()
    print("Tests Passed")
