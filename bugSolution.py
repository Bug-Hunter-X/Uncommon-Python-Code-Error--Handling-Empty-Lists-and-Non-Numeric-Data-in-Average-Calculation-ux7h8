def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")  # Output: Average: 0

# Example usage with a list of numbers
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"Average: {average}")  # Output: Average: 30.0

#Example usage with a list containing non-numeric values
numbers = [10,20,"a",30]
average = calculate_average(numbers)
print(f"Average: {average}") # Output: Average: 20.0