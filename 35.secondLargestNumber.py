def find_second_largest(nums):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[1]


my_list = [10, 5, 8, 20, 15]
second_largest = find_second_largest(my_list)
print(f"The second-largest number is: {second_largest}")
