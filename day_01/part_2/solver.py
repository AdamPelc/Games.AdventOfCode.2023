#!/usr/bin/python3

import sys

named_digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def solve_puzzle(puzzle_data):
    total = 0
    for line in puzzle_data:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        total = total + int(first_digit) * 10
        total = total + int(last_digit)
    print(f"Result: {total}")

def find_first_digit(line):
    pos = 99
    result = -1
    for index, named_digit in enumerate(named_digits):
        digit_pos = line.find(named_digit)
        if digit_pos != -1 and digit_pos < pos:
            pos = digit_pos
            result = index + 1
    for digit in range(10):
        digit_pos = line.find(str(digit))
        if digit_pos != -1 and digit_pos < pos:
            pos = digit_pos
            result = digit
    return result

def find_last_digit(line):
    pos = -1
    result = -1
    for index, named_digit in enumerate(named_digits):
        digit_pos = line.rfind(named_digit)
        if digit_pos != -1 and digit_pos > pos:
            pos = digit_pos
            result = index + 1
    for digit in range(10):
        digit_pos = line.rfind(str(digit))
        if digit_pos != -1 and digit_pos > pos:
            pos = digit_pos
            result = digit
    return result

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    file_data = file.readlines()
    solve_puzzle(file_data)

