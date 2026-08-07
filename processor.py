import json
from typing import Any, Dict, List


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save data as JSON to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_dict(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Return a dictionary with only the specified keys."""
    return {key: data[key] for key in keys if key in data}


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries into one."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]
