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

    # Directions for the first diagonal and second diagonal
    # Diagonal 1: top-left to bottom-right
    # Diagonal 2: bottom-left to top-right
    dir1 = [(-1, -1), (1, 1)]  # top-left to bottom-right and bottom-left to top-right
    dir2 = [(1, -1), (-1, 1)]  # bottom-left to top-right and top-right to bottom-left

    # Check for "MAS" or "SAM" in the diagonals
    def check_diagonal(word, row, col, dir1, dir2):
        m1_row, m1_col = row + dir1[0], col + dir1[1]  # top-left
        s1_row, s1_col = row + dir2[0], col + dir2[1]  # bottom-right
        m2_row, m2_col = row + dir2[0], col + dir2[1]  # bottom-left
        s2_row, s2_col = row + dir1[0], col + dir1[1]  # top-right

        # Check if positions are within bounds and the characters are the expected word
        if (0 <= m1_row < rows and 0 <= m1_col < cols and
            0 <= s1_row < rows and 0 <= s1_col < cols and
            0 <= m2_row < rows and 0 <= m2_col < cols and
            0 <= s2_row < rows and 0 <= s2_col < cols):
            
            if (grid[m1_row][m1_col] == word[0] and
                grid[row][col] == 'A' and
                grid[s1_row][s1_col] == word[1] and
                grid[m2_row][m2_col] == word[2] and
                grid[row][col] == 'A' and
                grid[s2_row][s2_col] == word[2]):
                return True
        return False

    # Check first diagonal (top-left -> bottom-right) and second diagonal (bottom-left -> top-right)
    if (check_diagonal('MAS', row, col, dir1, dir2) or check_diagonal('SAM', row, col, dir1, dir2)):
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
