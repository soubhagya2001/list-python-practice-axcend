import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy() 
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffled_result = shuffle_list(my_list)
print(f"Original List: {my_list}")
print(f"Shuffled List: {shuffled_result}")
