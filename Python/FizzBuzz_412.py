# Given an integer n, return a string array answer (1-indexed) where:
#   answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#   answer[i] == "Fizz" if i is divisible by 3.
#   answer[i] == "Buzz" if i is divisible by 5.
#   answer[i] == i (as a string) if none of the above conditions are true.

# Constraints:
# 1 <= n <= 104

import sys


class Solution:
    def fizzBuzz(n: int):

        fizzBuzz_maps = {3: "Fizz",
                         5: "Buzz"}

        return_list = []

        for i in range(1, n+1):
            current_string = ""

            for key in fizzBuzz_maps:
                if i % key == 0:
                    current_string += fizzBuzz_maps[key]

            if len(current_string) == 0:
                current_string += str(i)

            return_list.append(current_string)

        return return_list


if __name__ == "__main__":
    print(Solution.fizzBuzz(int(sys.argv[1])))
