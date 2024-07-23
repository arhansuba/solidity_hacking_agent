# testing/invariant_testing.py

from brownie import Contract, accounts
import hypothesis
from hypothesis import given, strategies as st

class ContractStateMachine(hypothesis.stateful.RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = Contract.from_abi("YourContract", "deployed_address", abi)
        self.balance = self.contract.balance()

    @hypothesis.stateful.rule(value=st.integers(min_value=1, max_value=100))
    def deposit(self, value):
        self.contract.deposit({'from': accounts[0], 'value': value})
        self.balance += value

    @hypothesis.stateful.rule(value=st.integers(min_value=1, max_value=100))
    def withdraw(self, value):
        if self.balance >= value:
            self.contract.withdraw(value, {'from': accounts[0]})
            self.balance -= value

    @hypothesis.stateful.invariant()
    def balance_matches(self):
        assert self.contract.balance() == self.balance, "Contract balance doesn't match expected balance"

TestContractStateMachine = ContractStateMachine.TestCase

# Usage
def test_invariants():
    hypothesis.settings.register_profile("invariant", max_examples=1000)
    hypothesis.settings.load_profile("invariant")
    TestContractStateMachine().runTest()

if __name__ == "__main__":
    test_invariants()