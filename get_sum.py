def calculate_sum(num_list):
    """
    This function takes a list of integers as input and returns the sum of those integers.
    """
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum

print(calculate_sum([1, 2, 3, 4, 5])) # Output: 15
