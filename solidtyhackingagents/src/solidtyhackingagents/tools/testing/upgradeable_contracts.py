# upgradeable_contracts.py

from web3 import Web3
from web3.middleware import geth_poa_middleware

class UpgradeableContractsManager:
    def __init__(self, provider_url: str, contract_address: str, abi: dict):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.web3.middleware_stack.inject(geth_poa_middleware, layer=0)
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def upgrade_contract(self, new_contract_address: str):
        """
        Upgrade the contract to a new address.
        """
        self.contract.address = Web3.toChecksumAddress(new_contract_address)
        print(f"Contract upgraded to {new_contract_address}")

    def interact_with_contract(self, function_name: str, *args):
        """
        Interact with a contract function.
        """
        function = getattr(self.contract.functions, function_name)
        result = function(*args).call()
        print(f"Result from {function_name}: {result}")

# Example usage
if __name__ == "__main__":
    provider_url = "https://your.ethereum.node"
    contract_address = "0xYourContractAddress"
    abi = [...]  # Replace with your contract ABI

    manager = UpgradeableContractsManager(provider_url, contract_address, abi)
    manager.interact_with_contract("yourFunctionName", "arg1", "arg2")
    manager.upgrade_contract("0xNewContractAddress")
