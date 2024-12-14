#!/usr/bin/env python3

def is_safe_report(report):
    # Check if the report is strictly increasing or decreasing
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    if not (increasing or decreasing):
        return False

    # Check if the difference between adjacent levels is between 1 and 3
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False

    return True

def main():
    safe_count = 0
    with open('../input/day2.txt', 'r') as file:
        for line in file:
            # Convert the space-separated numbers in the line to a list of integers
            report = list(map(int, line.split()))
            
            # Check if the report is safe
            if is_safe_report(report):
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
