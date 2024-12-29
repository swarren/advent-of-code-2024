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
    """Compacts the block map by moving file blocks to the leftmost free spaces."""
    free_index = 0
    file_blocks_to_move = [i for i, block in enumerate(block_map) if block is not None]

    for i in range(len(block_map)):
        if block_map[i] is None:  # Found a free space
            if file_blocks_to_move:
                last_file_index = file_blocks_to_move.pop()  # Get the last file block
                if last_file_index < i:  # Stop if no more blocks can be moved
                    break
                block_map[i] = block_map[last_file_index]  # Move it to the free space
                block_map[last_file_index] = None  # Clear the old position

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
