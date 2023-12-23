#!/usr/bin/python3

import sys
import re

def solve_puzzle(puzzle_data):
    result = 0
    for index, line in enumerate(puzzle_data):
        red = get_highest_color("red", line)
        green = get_highest_color("green", line)
        blue = get_highest_color("blue", line)
        tmp = red * green * blue
        result = result + tmp
    print(f"Result: {result}")

def get_highest_color(color, line):
    regex = fr"\d+(?=\s{color})"
    colors = re.findall(regex, line)
    highest_value = 0
    for color in colors:
        color_value = int(color)
        if color_value > highest_value:
            highest_value = color_value
    return highest_value

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    file_data = file.readlines()
    solve_puzzle(file_data)

