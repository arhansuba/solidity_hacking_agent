from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('IntegerUnderflowVulnerableContract.json') as f:
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

# Perform integer underflow attack
def perform_integer_underflow_attack(vulnerable_contract):
    # Trigger integer underflow condition
    tx_hash = vulnerable_contract.functions.triggerUnderflow().transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Integer underflow attack completed.")

perform_integer_underflow_attack(vulnerable_contract)
