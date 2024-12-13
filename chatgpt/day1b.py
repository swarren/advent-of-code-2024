#!/usr/bin/env python3
from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Step 1: Count the occurrences of each number in the right list
    right_list_counter = Counter(right_list)
    
    # Step 2: Calculate the similarity score
    similarity_score = sum(left * right_list_counter[left] for left in left_list)
    
    # Return the similarity score
    return similarity_score

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
    
    # Calculate and print the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity score:", similarity_score)
