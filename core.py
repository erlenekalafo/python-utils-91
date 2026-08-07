from typing import List, Any


def process_data(data: List[Any]) -> List[Any]:
    """
    Processes a list of data.
    
    Args:
        data (List[Any]): A list of data items to be processed.
    
    Returns:
        List[Any]: A list of processed data items.
    """
    return [item for item in data if item is not None]


def sum_numbers(numbers: List[float]) -> float:
    """
    Calculates the sum of a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to sum.
    
    Returns:
        float: The sum of the numbers.
    """
    return sum(numbers)


def find_max(numbers: List[float]) -> float:
    """
    Finds the maximum number in a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The maximum number in the list.
    """
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)


def is_even(number: int) -> bool:
    """
    Checks if a number is even.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0
