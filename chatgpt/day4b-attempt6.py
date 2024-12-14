#!/usr/bin/env python3

def read_input(file_path):
    # Read the grid from the given file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def check_xmas(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    
    # Check if we can form an X-MAS at (row, col) with center 'A'
    if grid[row][col] != 'A':
        return 0
    
    # Check for X-MAS in both directions
    # Direction 1: (Top-left to bottom-right and bottom-left to top-right)
    # Direction 2: (Bottom-left to top-right and top-left to bottom-right)
    
    # Check Top-left to bottom-right and bottom-left to top-right
    m1_row, m1_col = row - 1, col - 1  # Top-left M
    s1_row, s1_col = row + 1, col + 1  # Bottom-right S
    m2_row, m2_col = row + 1, col - 1  # Bottom-left M
    s2_row, s2_col = row - 1, col + 1  # Top-right S

    # Check if positions are within bounds and if the characters match the X-MAS pattern
    if (0 <= m1_row < rows and 0 <= m1_col < cols and
        0 <= s1_row < rows and 0 <= s1_col < cols and
        0 <= m2_row < rows and 0 <= m2_col < cols and
        0 <= s2_row < rows and 0 <= s2_col < cols):
        
        # Check if the letters form the correct pattern in both directions
        if (grid[m1_row][m1_col] == 'M' and grid[row][col] == 'A' and grid[s1_row][s1_col] == 'S' and
            grid[m2_row][m2_col] == 'M' and grid[row][col] == 'A' and grid[s2_row][s2_col] == 'S'):
            return 1

    return 0

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Traverse the grid to find the 'A' that could be the center of an X
    for row in range(1, rows-1):  # Avoid edge rows
        for col in range(1, cols-1):  # Avoid edge columns
            count += check_xmas(grid, row, col)
    
    return count

# Main code to execute
def main():
    file_path = '../input/day4.txt'
    grid = read_input(file_path)
    occurrences = count_xmas_patterns(grid)
    print(f"The X-MAS pattern appears {occurrences} times in the grid.")

# Run the main function
if __name__ == "__main__":
    main()
