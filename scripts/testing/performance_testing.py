# testing/performance_testing.py

import time
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor, as_completed

def measure_transaction_time(w3, contract, function_name, args, sender):
    start_time = time.time()
    tx_hash = contract.functions[function_name](*args).transact({'from': sender})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    end_time = time.time()
    return end_time - start_time

def performance_test(contract_address, abi, num_transactions=100, concurrency=10):
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    contract = w3.eth.contract(address=contract_address, abi=abi)
    
    def worker(i):
        return measure_transaction_time(w3, contract, 'someFunction', [i], w3.eth.accounts[0])
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(worker, i) for i in range(num_transactions)]
        times = [future.result() for future in as_completed(futures)]
    
    avg_time = sum(times) / len(times)
    print(f"Average transaction time: {avg_time:.4f} seconds")
    print(f"Transactions per second: {1/avg_time:.2f}")

# Usage
contract_address = "0x..."
abi = [...]  # Contract ABI
performance_test(contract_address, abi)