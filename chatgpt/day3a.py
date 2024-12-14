#!/usr/bin/env python3
import re

def main():
    # Read the input from the file
    with open('../input/day3.txt', 'r') as file:
        data = file.read()
    
    # Regular expression to find mul(X,Y) instructions
    # This matches 'mul(', followed by numbers (X and Y), and a closing ')'.
    pattern = r'mul\((\d+),(\d+)\)'
    
    total_sum = 0
    
    # Find all valid 'mul(X,Y)' patterns in the input string
    matches = re.findall(pattern, data)
    
    # For each match, multiply the two numbers and add to the total sum
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y
    
    print(total_sum)

if __name__ == "__main__":
    main()
