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

    count = 0
    # Define the relative directions for checking "MAS"
    directions = [
        [(-1, -1), (1, 1)],  # top-left -> bottom-right and bottom-left -> top-right
        [(1, -1), (-1, 1)],  # bottom-left -> top-right and top-right -> bottom-left
    ]
    
    # We need to check for two separate "MAS" words:
    # - "MAS" (forwards or backwards) in the top-left -> bottom-right direction
    # - "MAS" (forwards or backwards) in the bottom-left -> top-right direction
    for dir1, dir2 in directions:
        # First direction (m1 -> a -> s1)
        m1_row, m1_col = row + dir1[0], col + dir1[1]  # "M" in the first direction
        s1_row, s1_col = row + dir2[0], col + dir2[1]  # "S" in the second direction

        # Second direction (m2 -> a -> s2)
        m2_row, m2_col = row + dir2[0], col + dir2[1]  # "M" in the second direction
        s2_row, s2_col = row + dir1[0], col + dir1[1]  # "S" in the first direction

        # Check if all positions are within bounds
        if (0 <= m1_row < rows and 0 <= m1_col < cols and
            0 <= s1_row < rows and 0 <= s1_col < cols and
            0 <= m2_row < rows and 0 <= m2_col < cols and
            0 <= s2_row < rows and 0 <= s2_col < cols):
            
            # Check if the positions match the "MAS" pattern (forwards or backwards)
            if (grid[m1_row][m1_col] == 'M' and grid[row][col] == 'A' and grid[s1_row][s1_col] == 'S' and
                grid[m2_row][m2_col] == 'M' and grid[row][col] == 'A' and grid[s2_row][s2_col] == 'S'):
                count += 1

    return count

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
