def rearrange_digits(input_list: list[int]) -> list[int]:
    """
    Rearrange Array Elements so as to form two
    number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = quicksort(input_list)
    first_num = splitter(input_list, len(input_list)-1)
    second_num = splitter(input_list, len(input_list)-2)
    return [first_num, second_num]


def splitter(input_list: list[int], cut_index: int) -> int:
    value = 0
    while cut_index >= 0:
        value = value*10 + input_list[cut_index]
        cut_index -= 2
    return value


def quicksort(input_list: list[int]) -> list[int]:
    if len(input_list) < 2:
        return input_list
    else:
        pivot = input_list[0]
        first_half = [num for num in input_list[1:] if num <= pivot]
        second_half = [num for num in input_list[1:] if num > pivot]
        return quicksort(first_half) + [pivot] + quicksort(second_half)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[1, 2, 3, 4, 5], [964, 852]]
