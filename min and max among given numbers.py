def find_min_max():
    # Take input from the user
    numbers = input("Enter five numbers separated by spaces: ").split()
    
    # Convert the input strings to integers
    numbers = list(map(int, numbers))
    
    # Find the minimum and maximum numbers
    min_number = min(numbers)
    max_number = max(numbers)
    
    # Print the results
    print(f"max = {max_number}, min = {min_number}")

# Test Case 1
# Example Input: 1 3 5 7 2
# Expected Output: max = 7, min = 1
find_min_max()
