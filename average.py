from typing import Optional, Sequence, Union

Number = Union[int, float]


def calculate_average(numbers: Sequence[Number]) -> Optional[float]:
    """
    Calculate the arithmetic mean of a sequence of numbers.

    - Returns None for an empty sequence (backward-compatible behavior).
    - Validates that all elements are numeric (int or float) and not bools.

    Parameters
    ----------
    numbers: Sequence[Number]
        A finite sequence supporting len(...) with numeric values.

    Returns
    -------
    Optional[float]
        The arithmetic mean, or None if the sequence is empty.
    """

    if len(numbers) == 0:
        return None

    for index, value in enumerate(numbers):
        # Exclude bools explicitly since bool is a subclass of int.
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a valid number: {value!r}"
            )

    total: float = float(sum(numbers))
    average: float = total / len(numbers)
    return average


if __name__ == "__main__":
    # Example usage
    numbers_list = [10, 20, 30, 40]
    result = calculate_average(numbers_list)
    if result is not None:
        print(f"Среднее значение: {result}")
    else:
        print("Список пуст")


