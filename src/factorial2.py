def factorial(num: int) -> int:
    """Calculate the factorial of a number.
    Args:
        num (int): The number to calculate the factorial of.
    Returns:
        int: The factorial of the number.
    Example:
        >>> factorial(5)
        120
    """
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


if __name__ == "__main__":
    # print(factorial(5))
    assert factorial(5) == 120
    assert factorial(0) == 1
