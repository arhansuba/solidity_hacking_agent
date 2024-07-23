# scalability_testing.py

import time
import random
from typing import Callable, List

class ScalabilityTester:
    def __init__(self, test_function: Callable[[int], None]):
        self.test_function = test_function

    def test_scalability(self, load_sizes: List[int]):
        """
        Test scalability by increasing load sizes.
        """
        for load_size in load_sizes:
            print(f"Testing with load size: {load_size}")
            start_time = time.time()
            self.test_function(load_size)
            end_time = time.time()
            print(f"Time taken for load size {load_size}: {end_time - start_time} seconds")

# Example function to test
def example_scalability_test(load_size: int):
    # Simulate load
    data = [random.random() for _ in range(load_size)]
    sorted_data = sorted(data)

# Example usage
if __name__ == "__main__":
    tester = ScalabilityTester(example_scalability_test)
    tester.test_scalability([1000, 10000, 100000])
