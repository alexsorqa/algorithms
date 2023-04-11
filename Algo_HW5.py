"""Selection Sort
Implement the selection sort algorithm that is sorting in descending order.
"""


def selection_sort(arr: list):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list = [5, 3, 6, 1, 2, 9]
print(test_list)
print(selection_sort(test_list))


"""Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.
"""


def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list2 = [5, 3, 6, 1, 2, 9]
print(bubble_sort_descending(test_list2))


"""Insertion Sort
Implement the insertion sort algorithm that is sorting in descending order.
"""


def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_list3 = [5, 3, 6, 1, 2, 9]
print(insertion_sort_descending(test_list3))

"""Merge Sort
Implement the merge sort algorithm that is sorting in descending order.
"""


def merge_sort_descending(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort_descending(left_arr)
        merge_sort_descending(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


test_list3 = [5, 3, 6, 1, 2, 9]
print(merge_sort_descending(test_list3))