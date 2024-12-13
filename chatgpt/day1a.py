#!/usr/bin/env python3

def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)
    
    # Step 2: Calculate the total distance by summing the absolute differences of corresponding pairs
    total_distance = sum(abs(left - right) for left, right in zip(left_list_sorted, right_list_sorted))
    
    # Return the total distance
    return total_distance

def read_input_file(file_path):
    left_list = []
    right_list = []
    
    # Read the file and parse the numbers into two separate lists
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into two values and append them to the respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

# Main execution
if __name__ == "__main__":
    # Specify the input file path
    input_file = '../input/day1.txt'  # Your actual file path
    
    # Read and parse the input file
    left_list, right_list = read_input_file(input_file)
    
    # Calculate and print the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total distance:", total_distance)
