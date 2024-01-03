#!/usr/bin/python3

import sys
import re


class Number:
    def __init__(self):
        self.line_index: int = -1
        self.char_index_first: int = -1
        self.char_index_last: int = -1
        self.buffer = []
        self.is_part = False

    def __str__(self):
        return f"Number(line_index:{self.line_index}, char_index_first:{self.char_index_first}, char_index_last:{self.char_index_last}, buffer: {self.buffer})"

    def __repr__(self):
        return self.__str__()


def get_numbers(puzzle_data):
    numbers = []
    number = Number()
    create_new_number = True
    save_number = False
    for line_index, line in enumerate(puzzle_data):
        for char_index, char in enumerate(line):
            if re.match("[0-9]", char):
                if create_new_number:
                    number = Number()
                    number.line_index = line_index
                    number.char_index_first = char_index
                    number.buffer.append(char)
                    create_new_number = False
                    save_number = True
                else:
                    number.buffer.append(char)
            else:
                if save_number:
                    number.char_index_last = char_index - 1
                    numbers.append(number)
                    save_number = False
                    create_new_number = True
    return numbers


def get_part_numbers(numbers, puzzle_data):
    part_numbers = []
    for number in numbers:
        for line_index in range(number.line_index - 1, number.line_index + 2):
            if line_index < 0 or line_index >= len(puzzle_data):
                continue
            for char_index in range(number.char_index_first - 1, number.char_index_last + 2):
                if char_index < 0 or char_index >= len(puzzle_data[0]):
                    continue
                symbol = puzzle_data[line_index][char_index]
                if re.match("[^0-9\n\.]", symbol):
                    part_numbers.append(number)
    return part_numbers


def convert_to_true_number(number):
    true_number = 0
    for digit_index, digit in enumerate(reversed(number.buffer)):
        true_number = true_number + pow(10, digit_index) * int(digit)
    return true_number


def get_start_info(numbers, puzzle_data):
    gears = {}
    for number in numbers:
        for line_index in range(number.line_index - 1, number.line_index + 2):
            if line_index < 0 or line_index >= len(puzzle_data):
                continue
            for char_index in range(number.char_index_first - 1, number.char_index_last + 2):
                if char_index < 0 or char_index >= len(puzzle_data[0]):
                    continue
                symbol = puzzle_data[line_index][char_index]
                if "*" == symbol:
                    if (line_index, char_index) not in gears:
                        gears[(line_index, char_index)] = []
                    gears[(line_index, char_index)].append(convert_to_true_number(number))
    return gears


def get_gears_info(stars_info):
    total = 0
    for _, value in stars_info.items():
        if len(value) != 2:
            continue
        tmp = value[0] * value[1]
        total = total + tmp
    return total


def solve_puzzle(puzzle_data):
    all_numbers = get_numbers(puzzle_data)
    stars_info = get_start_info(all_numbers, puzzle_data)
    for key, value in stars_info.items():
        print(f"Key: {key}, Values: {value}")
    total = get_gears_info(stars_info)

    return total


file_path = sys.argv[1]


with open(file_path, 'r') as file:
    file_data = [[char for char in line] for line in file.readlines()]
    result = solve_puzzle(file_data)
    print(f"Result: {result}")

