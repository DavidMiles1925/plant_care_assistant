import os
from config import LOG_DIRECTORY_PATH

def count_water_dispensed(directory):
    # Initialize counters
    one_counter = 0
    two_counter = 0
    three_counter = 0

    # Iterate over each file in the specified directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), 'r') as file:
                # Read the file line by line
                for line in file:
                    # Look for the text "WATER DISPENSED:"
                    if "WATER DISPENSED:" in line:
                        # Find the position of "WATER DISPENSED:"
                        index = line.find("WATER DISPENSED:")
                        # Get the character 9 spaces to the right of it
                        char = line[index + 24]  # 25 = len("WATER DISPENSED:") + 9
                        # Increment the appropriate counter
                        if char == '1':
                            one_counter += 1
                        elif char == '2':
                            two_counter += 1
                        elif char == '3':
                            three_counter += 1

    # Print the results
    print(f"Count of '1': {one_counter}")
    print(f"Count of '2': {two_counter}")
    print(f"Count of '3': {three_counter}")


if __name__ == "__main__":

    # Set directory path appropriately
    directory_path = LOG_DIRECTORY_PATH

    # For windows...
    # directory_path = "C:/Users///"

    # Count the number of times water was dispensed for each sensor
    count_water_dispensed(directory_path)