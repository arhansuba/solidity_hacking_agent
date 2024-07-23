from web3 import Web3
import json

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Ensure connection is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Load vulnerable and attacker contract ABIs and bytecodes
with open('DelegatecallVulnerableContract.json') as f:
    contract_data = json.load(f)
vulnerable_abi = contract_data['abi']
vulnerable_bytecode = contract_data['bytecode']

with open('AttackerContract.json') as f:
    attacker_data = json.load(f)
attacker_abi = attacker_data['abi']
attacker_bytecode = attacker_data['bytecode']

def deploy_contract(abi, bytecode):
    # Create contract instance
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    
    # Transaction details
    tx = {
        'from': w3.eth.defaultAccount,
        'gas': 4000000,
        'gasPrice': w3.toWei('20', 'gwei'),
    }

    # Deploy contract
    try:
        tx_hash = contract.constructor().transact(tx)
        print(f"Contract deployment transaction hash: {tx_hash.hex()}")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")
        return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    except Exception as e:
        print(f"Error deploying contract: {e}")
        return None

def perform_delegatecall_attack(vulnerable_contract, attacker_contract):
    # Transaction details
    tx = {
        'from': w3.eth.defaultAccount,
        'gas': 4000000,
        'gasPrice': w3.toWei('20', 'gwei'),
    }

    try:
        # Perform delegatecall attack
        tx_hash = attacker_contract.functions.attack(vulnerable_contract.address).transact(tx)
        print(f"Attack transaction hash: {tx_hash.hex()}")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Delegatecall attack completed. Transaction receipt: {tx_receipt}")
    except Exception as e:
        print(f"Error performing delegatecall attack: {e}")

# Set default account (ensure this account has sufficient balance and is valid)
w3.eth.defaultAccount = w3.eth.accounts[0]  # Update as necessary

# Deploy vulnerable and attacker contracts
vulnerable_contract = deploy_contract(vulnerable_abi, vulnerable_bytecode)
attacker_contract = deploy_contract(attacker_abi, attacker_bytecode)

if vulnerable_contract and attacker_contract:
    # Perform delegatecall attack
    perform_delegatecall_attack(vulnerable_contract, attacker_contract)
else:
    print("Contract deployment failed. Attack not executed.")
