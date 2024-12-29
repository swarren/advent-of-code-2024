#!/usr/bin/env python3

from itertools import product

def parse_input(file_path):
    """Parses the input file and returns a list of test equations."""
    equations = []
    with open(file_path, 'r') as f:
        for line in f:
            test_value, numbers = line.split(":")
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((test_value, numbers))
    return equations

def evaluate_equation(numbers, operators):
    """Evaluates the equation formed by inserting operators between numbers."""
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    return result

def can_produce_test_value(test_value, numbers):
    """Checks if any combination of operators produces the test value."""
    num_operators = len(numbers) - 1
    for operators in product(['+', '*'], repeat=num_operators):
        if evaluate_equation(numbers, operators) == test_value:
            return True
    return False

def total_calibration_result(file_path):
    """Calculates the total calibration result."""
    equations = parse_input(file_path)
    total = 0
    for test_value, numbers in equations:
        if can_produce_test_value(test_value, numbers):
            total += test_value
    return total

def main():
    file_path = '../input/day7.txt'
    print(total_calibration_result(file_path))

if __name__ == "__main__":
    main()
