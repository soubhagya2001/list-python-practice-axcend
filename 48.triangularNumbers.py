def generate_triangular_numbers(n):
    triangular_numbers = [(i * (i + 1)) // 2 for i in range(1, n + 1)]
    return triangular_numbers


n = 5
triangular_numbers_list = generate_triangular_numbers(n)
print(f"The first {n} triangular numbers are: {triangular_numbers_list}")
