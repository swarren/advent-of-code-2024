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

    # Directions for the two diagonals (we need both diagonals to form "MAS" or "SAM")
    directions = [
        [(-1, -1), (1, 1)],  # top-left -> bottom-right and bottom-left -> top-right
        [(1, -1), (-1, 1)]   # bottom-left -> top-right and top-right -> bottom-left
    ]

    # Function to check a word on a diagonal
    def check_diagonal(word, row, col, direction):
        m_row, m_col = row + direction[0][0], col + direction[0][1]  # M direction
        s_row, s_col = row + direction[1][0], col + direction[1][1]  # S direction

        # Check if the positions are within bounds
        if 0 <= m_row < rows and 0 <= m_col < cols and 0 <= s_row < rows and 0 <= s_col < cols:
            # Check if the word matches (either forwards or backwards)
            return (grid[m_row][m_col] == word[0] and grid[row][col] == 'A' and grid[s_row][s_col] == word[2]) or \
                   (grid[m_row][m_col] == word[2] and grid[row][col] == 'A' and grid[s_row][s_col] == word[0])
        return False

    # We need to find two independent "MAS" words: one in each diagonal
    # Check if we can find "MAS" or "SAM" in both diagonals
    found_xmas = False
    for dir1 in directions:
        for word1 in ['MAS', 'SAM']:
            if check_diagonal(word1, row, col, dir1):
                for dir2 in directions:
                    for word2 in ['MAS', 'SAM']:
                        if dir1 != dir2 and check_diagonal(word2, row, col, dir2):
                            found_xmas = True
                            break
            if found_xmas:
                break
        if found_xmas:
            break

    return 1 if found_xmas else 0

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
