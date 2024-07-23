# testing_utils.py

import unittest

def run_tests(test_suite: unittest.TestSuite):
    """
    Run the given test suite.
    """
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

def assert_equal(expected, actual):
    """
    Assert that two values are equal.
    """
    assert expected == actual, f"Expected {expected}, but got {actual}"

def assert_in(item, container):
    """
    Assert that an item is in a container.
    """
    assert item in container, f"Item {item} not found in container"
