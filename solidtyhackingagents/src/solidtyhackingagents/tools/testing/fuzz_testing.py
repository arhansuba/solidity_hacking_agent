# fuzz_testing.py

import random
import string
from typing import Callable, List

class Fuzzer:
    def __init__(self, test_function: Callable[[str], None]):
        self.test_function = test_function

    def generate_random_input(self, length: int) -> str:
        """
        Generate random input for fuzz testing.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def fuzz_test(self, num_tests: int, input_length: int) -> List[str]:
        """
        Perform fuzz testing by generating random inputs and testing the function.
        """
        results = []
        for _ in range(num_tests):
            random_input = self.generate_random_input(input_length)
            try:
                self.test_function(random_input)
                results.append(f"Test with input '{random_input}' passed.")
            except Exception as e:
                results.append(f"Test with input '{random_input}' failed: {e}")
        return results

# Example function to test
def example_function(input_data: str):
    if len(input_data) > 10:
        raise ValueError("Input too long!")

# Example usage
if __name__ == "__main__":
    fuzzer = Fuzzer(example_function)
    test_results = fuzzer.fuzz_test(num_tests=10, input_length=20)
    for result in test_results:
        print(result)
