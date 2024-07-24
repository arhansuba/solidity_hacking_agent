# performance_testing.py

import time
import resource
from typing import Callable, Any

class PerformanceTester:
    def __init__(self, test_function: Callable[..., Any], *args, **kwargs):
        self.test_function = test_function
        self.args = args
        self.kwargs = kwargs

    def measure_performance(self):
        """
        Measure performance of the test function.
        """
        start_time = time.time()
        start_resources = resource.getrusage(resource.RUSAGE_SELF)

        result = self.test_function(*self.args, **self.kwargs)

        end_resources = resource.getrusage(resource.RUSAGE_SELF)
        end_time = time.time()

        elapsed_time = end_time - start_time
        cpu_time = end_resources.ru_utime - start_resources.ru_utime
        memory_usage = end_resources.ru_maxrss - start_resources.ru_maxrss

        print(f"Elapsed time: {elapsed_time} seconds")
        print(f"CPU time: {cpu_time} seconds")
        print(f"Memory usage: {memory_usage} kilobytes")

        return result

# Example function to test
def example_function(n: int):
    total = 0
    for i in range(n):
        total += i
    return total

# Example usage
if __name__ == "__main__":
    tester = PerformanceTester(example_function, 1000000)
    tester.measure_performance()
