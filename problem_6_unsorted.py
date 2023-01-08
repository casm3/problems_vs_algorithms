import random


def get_min_max(ints: list[int]) -> tuple[int]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = ints[0]
    max_value = ints[0]
    for value in ints:
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value

    return (min_value, max_value)


# Example Test Case of Ten Integers
list_of_ints = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(list_of_ints)

print("Pass" if ((0, 9) == get_min_max(list_of_ints)) else "Fail")
