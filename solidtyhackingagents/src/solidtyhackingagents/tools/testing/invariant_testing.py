# invariant_testing.py

from typing import Callable, List

class InvariantTester:
    def __init__(self, invariants: List[Callable[[], bool]]):
        self.invariants = invariants

    def test_invariants(self):
        """
        Test all invariants and report if any fail.
        """
        for i, invariant in enumerate(self.invariants):
            try:
                if not invariant():
                    print(f"Invariant {i} failed!")
            except Exception as e:
                print(f"Invariant {i} exception: {e}")

# Example invariants
def invariant_example1() -> bool:
    return True  # Replace with actual invariant check

def invariant_example2() -> bool:
    return 1 + 1 == 2  # Replace with actual invariant check

# Example usage
if __name__ == "__main__":
    invariants = [invariant_example1, invariant_example2]
    tester = InvariantTester(invariants)
    tester.test_invariants()
