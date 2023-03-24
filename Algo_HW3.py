"""Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
"""


def arithmetical_mean(arr: list):
    return [x for x in arr if x <= sum(arr) / len(arr)]


print(arithmetical_mean([1, 3, 5, 6, 4, 10, 2, 3]))


"""Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
"""


def lowest_elements(arr2: list):
    arr2.sort()
    return f"{arr2[0]}, {arr2[1]}"


print(lowest_elements([198, 3, 4, 9, 10, 9, 2]))