#!/usr/bin/env python3

def parse_input(file_path):
    """Reads the disk map from the input file."""
    with open(file_path, 'r') as f:
        return f.read().strip()

def convert_disk_map_to_block_map(disk_map):
    """Converts the compact disk map to a block map."""
    block_map = []
    file_id = 0
    for i, length in enumerate(map(int, disk_map)):
        if i % 2 == 0:  # File length
            block_map.extend([file_id] * length)
            file_id += 1
        else:  # Free space length
            block_map.extend([None] * length)
    return block_map

def compact_block_map(block_map):
    """Compacts the block map by moving whole files to the leftmost free spaces."""
    file_ids = sorted(set(block for block in block_map if block is not None), reverse=True)

    for file_id in file_ids:
        # Get indices of the current file
        file_indices = [i for i, block in enumerate(block_map) if block == file_id]
        file_length = len(file_indices)

        # Find the leftmost span of free space that can fit the file, before the file's current position
        for i in range(len(block_map) - file_length + 1):
            if all(block is None for block in block_map[i:i + file_length]) and i + file_length <= file_indices[0]:
                # Move the file to this span
                for j, file_index in enumerate(file_indices):
                    block_map[i + j] = file_id
                    block_map[file_index] = None
                break

    return block_map

def calculate_checksum(block_map):
    """Calculates the checksum of the compacted block map."""
    return sum(index * block for index, block in enumerate(block_map) if block is not None)

def main():
    file_path = '../input/day9.txt'
    disk_map = parse_input(file_path)
    block_map = convert_disk_map_to_block_map(disk_map)
    compacted_block_map = compact_block_map(block_map)
    checksum = calculate_checksum(compacted_block_map)
    print(checksum)

if __name__ == "__main__":
    main()
