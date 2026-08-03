import time
from functools import lru_cache

@lru_cache(maxsize=1024)
def heavy_computation(data):
    # Simulated expensive computation
    time.sleep(1)  # Simulating time delay
    return sum(data)  # Returning sum as the result

class Processor:
    def __init__(self, data):
        self.data = data
        self.results = []

    def process_data(self):
        for item in self.data:
            # Using memoization for performance
            result = heavy_computation(tuple(item))
            self.results.append(result)

    def get_results(self):
        return self.results

if __name__ == '__main__':
    data = [list(range(1000))] * 10  # Sample data with repeats
    processor = Processor(data)
    processor.process_data()
    print(processor.get_results())