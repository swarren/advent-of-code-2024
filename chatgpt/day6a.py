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
    """Simulates the guard's patrol and returns the number of distinct positions visited."""
    rows, cols = len(lab_map), len(lab_map[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    # Find guard start position and direction
    r, c, direction = find_guard_start(lab_map)
    direction_idx = directions.index(direction)

    visited = set()
    visited.add((r, c))

    while 0 <= r < rows and 0 <= c < cols:
        dr, dc = directions[direction_idx]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and lab_map[nr][nc] != '#':
            r, c = nr, nc
        else:
            direction_idx = (direction_idx + 1) % 4  # Turn right

        visited.add((r, c))

        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            break

    return len(visited)

def main():
    file_path = '../input/day6.txt'
    lab_map = parse_map(file_path)
    print(simulate_guard_path(lab_map))

if __name__ == "__main__":
    main()
