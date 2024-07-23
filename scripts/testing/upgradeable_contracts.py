# testing/upgradeable_contracts.py

from brownie import Contract, project, accounts

def test_upgradeable_contract():
    # Load the project
    p = project.load('.')
    p.load_config()
    
    # Deploy the initial version
    initial_contract = p.YourContract.deploy({'from': accounts[0]})
    proxy = p.TransparentUpgradeableProxy.deploy(
        initial_contract.address,
        accounts[0],
        b'',
        {'from': accounts[0]}
    )
    
    # Interact with the proxy
    contract = Contract.from_abi("YourContract", proxy.address, initial_contract.abi)
    initial_value = contract.someFunction()
    
    # Deploy the upgraded version
    upgraded_contract = p.YourContractV2.deploy({'from': accounts[0]})
    
    # Upgrade the proxy
    proxy.upgradeTo(upgraded_contract.address, {'from': accounts[0]})
    
    # Verify the upgrade
    contract = Contract.from_abi("YourContractV2", proxy.address, upgraded_contract.abi)
    assert contract.someFunction() == initial_value
    assert contract.newFunction() == 42  # New function in V2

# Usage
def main():
    test_upgradeable_contract()

if __name__ == "__main__":
    main()