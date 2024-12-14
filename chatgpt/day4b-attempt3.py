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
    
    count = 0
    # Directions for checking "MAS" pattern
    directions = [
        # Top-left to bottom-right and Bottom-left to top-right
        [(-1, -1), (1, 1)],  # forward direction (M, A, S) and reverse (S, A, M)
        [(1, -1), (-1, 1)],  # reverse direction (S, A, M) and forward (M, A, S)
    ]
    
    # For each pair of directions
    for dir1, dir2 in directions:
        # Check the first part of the X (M -> A)
        m1_row, m1_col = row + dir1[0], col + dir1[1]
        s1_row, s1_col = row + dir2[0], col + dir2[1]
        
        # Check if the positions are within bounds
        if (0 <= m1_row < rows and 0 <= m1_col < cols and
            0 <= s1_row < rows and 0 <= s1_col < cols):
            
            # Check the pattern in both directions
            if (grid[m1_row][m1_col] == 'M' and grid[row][col] == 'A' and grid[s1_row][s1_col] == 'S'):
                count += 1
            if (grid[s1_row][s1_col] == 'M' and grid[row][col] == 'A' and grid[m1_row][m1_col] == 'S'):
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
