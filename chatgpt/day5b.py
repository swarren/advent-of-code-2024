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

def reorder_update(update, rules):
    """Reorders a single update based on the rules."""
    # Create a dependency graph
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1

    # Perform topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def main():
    file_path = '../input/day5.txt'
    rules, updates = parse_input(file_path)

    total_middle_pages = 0

    for update in updates:
        if is_update_ordered(update, rules):
            continue
        
        corrected_update = reorder_update(update, rules)
        total_middle_pages += find_middle_page(corrected_update)

    print("Total middle page sum of correctly ordered incorrect updates:", total_middle_pages)

if __name__ == "__main__":
    main()
