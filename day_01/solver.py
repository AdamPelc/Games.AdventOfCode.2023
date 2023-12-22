#!/usr/bin/python3

import sys

def solve_puzzle(puzzle_data):
    total = 0
    for line in puzzle_data:
        first_digit = 0
        last_digit = 0
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break
        total = total + int(first_digit) * 10
        total = total + int(last_digit)
    print(f"Result: {total}")

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    file_data = file.readlines()
    solve_puzzle(file_data)

