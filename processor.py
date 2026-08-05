import time
import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        start_time = time.time()
        self.data = np.array(self.data)
        # Normalizing data to improve processing
        self.data = (self.data - np.mean(self.data)) / np.std(self.data)
        end_time = time.time()
        print(f"Preprocessing time: {end_time - start_time:.4f} seconds")

    def process(self):
        start_time = time.time()
        # Using vectorized operations for performance
        result = np.sum(self.data ** 2)
        end_time = time.time()
        print(f"Processing time: {end_time - start_time:.4f} seconds")
        return result

# Example usage
if __name__ == '__main__':
    raw_data = [i for i in range(100000)]  # Example data
    processor = DataProcessor(raw_data)
    processor.preprocess()
    result = processor.process()
    print(f"Result of processing: {result}")