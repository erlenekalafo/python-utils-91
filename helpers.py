from typing import Any, Dict, Union
import json


def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: The parsed JSON data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data as JSON to a file.

    Args:
        data (Dict[str, Any]): The data to save.
        file_path (str): The path where to save the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def calculate_percentage(part: Union[int, float], whole: Union[int, float]) -> float:
    """
    Calculate the percentage of a part relative to a whole.

    Args:
        part (Union[int, float]): The part to consider.
        whole (Union[int, float]): The whole to base the percentage on.

    Returns:
        float: The calculated percentage.
    """
    return (part / whole) * 100 if whole else 0.0
