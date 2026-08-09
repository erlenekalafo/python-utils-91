import json
from typing import Any, Dict


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f'Error: The file {file_path} was not found.')
    except json.JSONDecodeError:
        raise Exception(f'Error: The file {file_path} does not contain valid JSON.')


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save data as JSON to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries with dict2 overwriting dict1 values."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary with a custom separator."""
    items = {}
    for k, v in data.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items
