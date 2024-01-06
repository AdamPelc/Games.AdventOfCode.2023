import math
import sys
import re


def solve_puzzle(puzzle_data):
    result = 0
    for line_idx, line in enumerate(puzzle_data):
        winning_numbers = [int(number) for number in re.search(r":\s*(.*?)\s*\|", line).group(1).split()]
        my_numbers = [int(number) for number in re.search(r"\|\s*(.*)", line).group(1).split()]
        amount_of_common_numbers = len(set(winning_numbers) & set(my_numbers))
        result += math.floor(2 ** (amount_of_common_numbers - 1))
        print(f"Card\t{line_idx}: amount_of_common_numbers: {amount_of_common_numbers}. Points: {math.floor(2 ** (amount_of_common_numbers - 1))}")
    return result


file_path = sys.argv[1]


with open(file_path, 'r') as file:
    file_data = file.readlines()
    result = solve_puzzle(file_data)
    print(f"Result: {result}")

