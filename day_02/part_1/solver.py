#!/usr/bin/python3

import sys
import re

named_digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def solve_puzzle(puzzle_data):
    result = 0
    for index, line in enumerate(puzzle_data):
        is_red = is_red_ok(line)
        is_green = is_green_ok(line)
        is_blue = is_blue_ok(line)
        if is_red and is_green and is_blue:
            result = result + index + 1
    print(f"Result: {result}")

def is_red_ok(line):
    max_reds = 12
    reds = re.findall("\d+(?=\sred)", line)
    for red in reds:
        if int(red) > max_reds:
            return False
    return True

def is_green_ok(line):
    max_greens = 13
    greens = re.findall("\d+(?=\sgreen)", line)
    for green in greens:
        if int(green) > max_greens:
            return False
    return True

def is_blue_ok(line):
    max_blues = 14
    blues = re.findall("\d+(?=\sblue)", line)
    for blue in blues:
        if int(blue) > max_blues:
            return False
    return True

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    file_data = file.readlines()
    solve_puzzle(file_data)

