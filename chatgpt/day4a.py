#!/usr/bin/env python3

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Define all 8 possible directions: (row_offset, col_offset)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    # Function to check if "XMAS" can be found starting from (r, c) in a given direction
    def is_xmas(r, c, dr, dc):
        for i in range(target_len):
            nr, nc = r + dr * i, c + dc * i
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target[i]:
                return False
        return True

    # Iterate over each position in the grid
    for r in range(rows):
        for c in range(cols):
            # For each direction, check if "XMAS" can be formed starting from (r, c)
            for dr, dc in directions:
                if is_xmas(r, c, dr, dc):
                    count += 1

    return count

def main():
    # Read the input from the file
    with open('../input/day4.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    # Find the total occurrences of "XMAS"
    result = find_xmas(grid)
    
    print(result)

if __name__ == "__main__":
    main()
