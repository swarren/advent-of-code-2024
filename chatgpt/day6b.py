#!/usr/bin/env python3

def parse_map(file_path):
    """Parses the input file and returns the map as a 2D list."""
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_guard_start(lab_map):
    """Finds the starting position and direction of the guard."""
    for r, row in enumerate(lab_map):
        for c, cell in enumerate(row):
            if cell == '^':
                return r, c, (-1, 0)  # Facing up
    raise ValueError("Guard starting position not found")

def simulate_guard_path(lab_map):
    """Simulates the guard's patrol and returns True if a loop is detected, False if the guard leaves the map."""
    rows, cols = len(lab_map), len(lab_map[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    # Find guard start position and direction
    r, c, direction = find_guard_start(lab_map)
    direction_idx = directions.index(direction)

    visited_set = set()
    visited_set.add((r, c, direction_idx))

    while True:
        dr, dc = directions[direction_idx]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):  # Guard left the map
            return False

        if lab_map[nr][nc] != '#':  # Move forward if no obstacle
            r, c = nr, nc
        else:  # Turn right if there's an obstacle
            direction_idx = (direction_idx + 1) % 4

        if (r, c, direction_idx) in visited_set:  # Loop detected
            return True

        visited_set.add((r, c, direction_idx))

def find_loop_positions(lab_map):
    """Finds positions where placing an obstruction would cause the guard to get stuck in a loop."""
    rows, cols = len(lab_map), len(lab_map[0])
    start_r, start_c, _ = find_guard_start(lab_map)
    loop_positions = set()

    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] == '.' and (r, c) != (start_r, start_c):  # Can't place at the start position
                # Temporarily place an obstruction
                lab_map[r][c] = '#'
                if simulate_guard_path(lab_map):
                    loop_positions.add((r, c))
                lab_map[r][c] = '.'  # Remove the obstruction

    return len(loop_positions)

def main():
    file_path = '../input/day6.txt'
    lab_map = parse_map(file_path)
    print(find_loop_positions(lab_map))

if __name__ == "__main__":
    main()
