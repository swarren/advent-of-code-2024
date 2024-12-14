#!/usr/bin/env python3
import re

def main():
    # Read the input from the file
    with open('../input/day3.txt', 'r') as file:
        data = file.read()
    
    # Regular expression to find mul(X,Y) instructions
    pattern_mul = r'mul\((\d+),(\d+)\)'
    # Regular expressions to find 'do()' and 'don\'t()' instructions
    pattern_do = r'do\(\)'
    pattern_dont = r"don't\(\)"
    
    total_sum = 0
    enabled = True  # Initially, mul instructions are enabled
    
    # Find all occurrences of 'do()', 'don't()', and 'mul(X,Y)'
    i = 0
    while i < len(data):
        # Look for the next 'do()', 'don't()', or 'mul(X,Y)'
        if re.match(pattern_do, data[i:]):
            # If 'do()' is found, enable future multiplications
            enabled = True
            i += len("do()")
        elif re.match(pattern_dont, data[i:]):
            # If 'don't()' is found, disable future multiplications
            enabled = False
            i += len("don't()")
        elif re.match(pattern_mul, data[i:]):
            # If 'mul(X,Y)' is found, process it if enabled
            match = re.search(pattern_mul, data[i:])
            if match:
                x, y = int(match.group(1)), int(match.group(2))
                if enabled:
                    total_sum += x * y
                i += match.end()  # Move past the current mul instruction
        else:
            # If no instruction matches, move to the next character
            i += 1
    
    print(total_sum)

if __name__ == "__main__":
    main()
