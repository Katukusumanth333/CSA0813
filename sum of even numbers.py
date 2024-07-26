def sum_of_even_numbers(n):
    sum_even = 0
    for i in range(1, n + 1):
        sum_even += 2 * i
    return sum_even
n = 10  
result = sum_of_even_numbers(n)
print(f"The sum of the first {n} even numbers is: {result}")

