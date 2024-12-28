#!/usr/bin/env python3

def parse_input(file_path):
    """Parses the input file and returns ordering rules and updates."""
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')

    # Split the input into rules and updates
    rules = []
    updates = []
    in_updates = False

    for line in lines:
        if line.strip() == "":
            in_updates = True
        elif in_updates:
            updates.append(list(map(int, line.split(','))))
        else:
            rules.append(tuple(map(int, line.split('|'))))

    return rules, updates

def is_update_ordered(update, rules):
    """Checks if a single update is in the correct order based on the rules."""
    # Create a position map for the update
    position = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False

    return True

def find_middle_page(update):
    """Returns the middle page of the update."""
    return update[len(update) // 2]

def main():
    file_path = '../input/day5.txt'
    rules, updates = parse_input(file_path)

    total_middle_pages = 0

    for update in updates:
        if is_update_ordered(update, rules):
            total_middle_pages += find_middle_page(update)

    print("Total middle page sum of correctly ordered updates:", total_middle_pages)

if __name__ == "__main__":
    main()
