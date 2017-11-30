# Task

# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list. If there are
# multiple elements with the same value, remove the one
# with a lower index. If you get an empty array/list,
# return an empty array/list. Don't change the order of
# the elements that are left.

# Solution


def remove_smallest(numbers):
    if len(numbers) > 0:
        smallest = numbers[0]
        for x in range(1, len(numbers)):
            if numbers[x] < smallest:
                smallest = numbers[x]
        numbers.remove(smallest)
        return numbers
    return []

# Best solution


def remove_smallest_(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers
