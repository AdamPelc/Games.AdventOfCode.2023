import math
import sys
import re


def solve_puzzle(puzzle_data):
    scratchcards_amount = [1] * len(puzzle_data)
    print(scratchcards_amount)
    for line_idx, line in enumerate(puzzle_data):
        winning_numbers = [int(number) for number in re.search(r":\s*(.*?)\s*\|", line).group(1).split()]
        my_numbers = [int(number) for number in re.search(r"\|\s*(.*)", line).group(1).split()]
        amount_of_common_numbers = len(set(winning_numbers) & set(my_numbers))
        for i in range(line_idx + 1, line_idx + amount_of_common_numbers + 1):
            scratchcards_amount[i] += scratchcards_amount[line_idx]
        print(scratchcards_amount)
    return sum(scratchcards_amount)


file_path = sys.argv[1]


with open(file_path, 'r') as file:
    file_data = file.readlines()
    result = solve_puzzle(file_data)
    print(f"Result: {result}")

