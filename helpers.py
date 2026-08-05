def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    for key, value in data.items():
        if not isinstance(key, str):
            raise ValueError('All keys must be strings')
        if not isinstance(value, (int, float, str)):
            raise ValueError('All values must be int, float, or str')

def process_data(data):
    validate_input(data)
    results = {}
    for key, value in data.items():
        # Simple processing logic for demonstration
        results[key] = value * 2 if isinstance(value, (int, float)) else value.upper()
    return results

if __name__ == '__main__':
    input_data = {'a': 1, 'b': 2.5, 'c': 'text', 'd': 4}
    try:
        processed = process_data(input_data)
        print(processed)
    except ValueError as e:
        print(f'Error: {e}')