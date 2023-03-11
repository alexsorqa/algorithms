"""Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15"""
def compute_digits(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(compute_digits(5))

"""Find the max number from 3 values.
Example: 124, 21, 32. Result = 124."""
def find_max(a: int, b: int, c: int):
    return max(a,b,c)
print(find_max(124, 21, 32))

"""Count odd and even numbers. Count odd and even digits of the whole number.
Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
"""
def count_odd_even(num: int):
    print(f"Total even digits: {len([int(elem) for elem in str(num) if int(elem) % 2 == 0])}", end=' AND ')
    print(f"Total odd digits: {len([int(elem) for elem in str(num) if int(elem) % 2 != 0])}")
count_odd_even(34560)