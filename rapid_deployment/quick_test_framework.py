# quick_test_framework.py

import unittest
from typing import List, Callable

class QuickTestFramework:
    def __init__(self):
        self.tests = []

    def add_test(self, name: str, test_function: Callable) -> None:
        """
        Add a test to the framework.
        """
        self.tests.append((name, test_function))

    def run_tests(self) -> None:
        """
        Run all added tests and report results.
        """
        print("Running tests...")
        suite = unittest.TestSuite()
        for name, test_function in self.tests:
            test_case = self.create_test_case(name, test_function)
            suite.addTest(test_case)
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def create_test_case(self, name: str, test_function: Callable) -> unittest.TestCase:
        """
        Create a unittest.TestCase for the provided test function.
        """
        class TestCase(unittest.TestCase):
            def runTest(self):
                test_function()

        TestCase.__name__ = name
        return TestCase()

# Example usage
if __name__ == "__main__":
    framework = QuickTestFramework()

    def test_sql_injection():
        assert True  # Replace with actual test logic

    def test_xss():
        assert False  # Replace with actual test logic

    framework.add_test("SQL Injection Test", test_sql_injection)
    framework.add_test("XSS Test", test_xss)
    framework.run_tests()
