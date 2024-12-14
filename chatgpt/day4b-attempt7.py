#!/usr/bin/env python3

def read_input(file_path):
    # Read the grid from the given file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def check_xmas(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    
    # Check if the center is 'A'
    if grid[row][col] != 'A':
        return 0
    
    # Check all 4 diagonal directions and whether each word can be forwards or backwards
    # Directions for the arms of the X
    directions = [
        [(-1, -1), (1, 1)],  # top-left -> bottom-right and bottom-left -> top-right
        [(1, -1), (-1, 1)],  # bottom-left -> top-right and top-right -> bottom-left
    ]
    
    # For each pair of diagonal directions, check both forward and backward MAS possibilities
    for dir1, dir2 in directions:
        # Check top-left to bottom-right (dir1) and bottom-left to top-right (dir2)
        m1_row, m1_col = row + dir1[0], col + dir1[1]  # "M" top-left
        s1_row, s1_col = row + dir2[0], col + dir2[1]  # "S" bottom-right
        
        m2_row, m2_col = row + dir2[0], col + dir2[1]  # "M" bottom-left
        s2_row, s2_col = row + dir1[0], col + dir1[1]  # "S" top-right

        # Check if positions are within bounds
        if (0 <= m1_row < rows and 0 <= m1_col < cols and
            0 <= s1_row < rows and 0 <= s1_col < cols and
            0 <= m2_row < rows and 0 <= m2_col < cols and
            0 <= s2_row < rows and 0 <= s2_col < cols):
            
            # Check if the pattern forms a valid X-MAS in both directions
            if (grid[m1_row][m1_col] == 'M' and grid[row][col] == 'A' and grid[s1_row][s1_col] == 'S' and
                grid[m2_row][m2_col] == 'M' and grid[row][col] == 'A' and grid[s2_row][s2_col] == 'S'):
                return 1
    
    # If no valid X-MAS pattern found, return 0
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
