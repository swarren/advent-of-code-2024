#!/usr/bin/env python3

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # We need at least 3 rows and 3 columns to form a valid X-MAS pattern
    if rows < 3 or cols < 3:
        return count

    # Iterate over each possible center point of the X-MAS pattern
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check for the X-MAS pattern (M . S, . A ., M . S)
            if grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S' and \
               grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S' and \
               grid[r][c] == 'A':
                count += 1

            # Check for the reverse X-MAS pattern (S . M, . A ., S . M)
            if grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M' and \
               grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M' and \
               grid[r][c] == 'A':
                count += 1

    return count

def main():
    # Read the input from the file
    with open('../input/day4.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    # Find the total occurrences of the X-MAS pattern
    result = find_xmas(grid)
    
    print(result)

if __name__ == "__main__":
    main()
