# testing/scalability_testing.py

import asyncio
import aiohttp
from web3 import Web3

async def send_transaction(session, w3, contract, function_name, args, sender, nonce):
    tx = contract.functions[function_name](*args).build_transaction({
        'from': sender,
        'nonce': nonce,
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    async with session.post('http://localhost:8545', json={
        "jsonrpc": "2.0",
        "method": "eth_sendRawTransaction",
        "params": [signed_tx.rawTransaction.hex()],
        "id": 1
    }) as resp:
        return await resp.json()

async def scalability_test(contract_address, abi, num_transactions=1000, batch_size=100):
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    contract = w3.eth.contract(address=contract_address, abi=abi)
    sender = w3.eth.accounts[0]
    private_key = '0x...'  # Private key for sender
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(0, num_transactions, batch_size):
            batch = []
            for j in range(batch_size):
                if i + j < num_transactions:
                    nonce = w3.eth.get_transaction_count(sender) + i + j
                    task = send_transaction(session, w3, contract, 'someFunction', [i+j], sender, nonce)
                    batch.append(task)
            tasks.append(asyncio.gather(*batch))
        
        results = await asyncio.gather(*tasks)
    
    print(f"Sent {num_transactions} transactions in {len(tasks)} batches")

# Usage
contract_address = "0x..."
abi = [...]  # Contract ABI
asyncio.run(scalability_test(contract_address, abi))