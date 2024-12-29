#!/usr/bin/env python3

def parse_disk_map(file_path):
    """Parses the input file and returns the disk map as a list of integers."""
    with open(file_path, 'r') as f:
        return [int(char) for char in f.read().strip()]

def compact_disk(disk_map):
    """Compacts the disk by moving file blocks to the leftmost free space."""
    compacted = []
    for i in range(0, len(disk_map), 2):
        file_blocks = [disk_map[i]] * disk_map[i]
        compacted.extend(file_blocks)
    compacted.extend([0] * (len(disk_map) - len(compacted)))  # Fill with free space
    return compacted

def calculate_checksum(compacted_map):
    """Calculates the filesystem checksum."""
    checksum = 0
    for position, block in enumerate(compacted_map):
        if block != 0:  # Skip free space
            checksum += position * block
    return checksum

def main():
    file_path = "../input/day9.txt"
    disk_map = parse_disk_map(file_path)
    compacted_map = compact_disk(disk_map)
    checksum = calculate_checksum(compacted_map)
    print(f"Filesystem checksum: {checksum}")

if __name__ == "__main__":
    main()
