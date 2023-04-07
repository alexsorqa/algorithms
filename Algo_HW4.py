"""Even First
Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
"""


def even_first(arr: list):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            for j in range(i, len(arr)):
                if arr[j] % 2 == 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
    odd_index = 0
    for k in range(len(arr)):
        if arr[k] % 2 != 0:
            odd_index = k
            break
    arr = arr[:odd_index] + arr[:odd_index - 1:-1]
    print(arr)


even_first([7, 3, 5, 6, 4, 10, 3, 2])

"""
Increment a Number
Write a program that takes as input a list of digits encoding a non-negative decimal integer D and updates the list to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
"""


def increment_a_number(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        arr = [str(i) for i in arr]
        arr = int(''.join(arr)) + 1
        arr = list(str(arr))
        arr = [int(i) for i in arr]
        return arr


print(increment_a_number([1, 2, 9]))

