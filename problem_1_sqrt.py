def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        if int(number) < 0:
            raise TypeError
    except TypeError:
        return None

    if number <= 1:
        return number

    y: int = number
    z: int = (y + 1) // 2

    while z < y:
        y = z
        z = (y + (number // y)) // 2
    return y


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (100 == sqrt(10000)) else "Fail")
print("Pass" if (None is sqrt([])) else "Fail")
print("Pass" if (None is sqrt(None)) else "Fail")
print("Pass" if (None is sqrt(-9)) else "Fail")
