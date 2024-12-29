#!/usr/bin/env python3

def parse_input(file_path):
    """Parses the input file and returns a map of antenna frequencies."""
    antenna_map = []
    with open(file_path, 'r') as f:
        for line in f:
            antenna_map.append(line.strip())
    return antenna_map

def find_antennas(antenna_map):
    """Finds all antennas and their frequencies on the map."""
    antennas = []
    for r, row in enumerate(antenna_map):
        for c, char in enumerate(row):
            if char.isalnum():  # Check for letters and digits
                antennas.append((r, c, char))
    return antennas

def calculate_antinodes(antenna_map, antennas):
    """Calculates all unique antinode positions within map bounds."""
    rows, cols = len(antenna_map), len(antenna_map[0])
    antinodes = set()

    for i, (r1, c1, freq1) in enumerate(antennas):
        # Calculate antinodes based on alignment with other antennas of the same frequency
        for j, (r2, c2, freq2) in enumerate(antennas):
            if i >= j or freq1 != freq2:
                continue

            # Calculate delta and iterate to find all antinodes along the line
            dr, dc = r2 - r1, c2 - c1

            # Check in the negative direction
            k = 0
            while True:
                antinode = (r1 - k * dr, c1 - k * dc)
                if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                    antinodes.add(antinode)
                else:
                    break
                k += 1

            # Check in the positive direction
            k = 0
            while True:
                antinode = (r2 + k * dr, c2 + k * dc)
                if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                    antinodes.add(antinode)
                else:
                    break
                k += 1

    return antinodes

def count_unique_antinodes(file_path):
    """Counts the number of unique antinode positions on the map."""
    antenna_map = parse_input(file_path)
    antennas = find_antennas(antenna_map)
    antinodes = calculate_antinodes(antenna_map, antennas)
    return len(antinodes)

def main():
    file_path = '../input/day8.txt'
    print(count_unique_antinodes(file_path))

if __name__ == "__main__":
    main()
