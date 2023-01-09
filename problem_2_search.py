def binary_search(input_list: list, number: int) -> int:
    low: int = 0
    high: int = len(input_list) - 1

    while high >= low:
        mid: int = low + (high - low) // 2
        guess: int = input_list[mid]

        if guess == number:
            return mid

        if input_list[low] <= guess:
            if number >= input_list[low] and number < guess:
                high = mid
            else:
                low = mid + 1
        else:
            if number <= input_list[high] and number > guess:
                low = mid + 1
            else:
                high = mid
    return -1


def rotated_array_search(input_list: list, number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search(input_list, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(
        input_list,
        number
    ) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[10, 7, 8, 9, 11, 1, 2, 3, 4], 1])
test_function([[-3, -2, -1, 0, 1, 2, 3], 0])
test_function([[-1, 0, 1, 2, 3], 4])
