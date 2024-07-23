from web3 import Web3
from eth_account import Account
from hexbytes import HexBytes

# Connect to Ethereum node (replace with your node URL)
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Smart contract details
CONTRACT_ADDRESS = '0xYourSmartContractAddress'
ABI = [...]  # Replace with the ABI of your smart contract

# Wallets and private keys
USER_PRIVATE_KEY = '0xYourUserPrivateKey'
ADMIN_PRIVATE_KEY = '0xYourAdminPrivateKey'

# Load contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def get_account(private_key):
    account = Account.from_key(private_key)
    return account.address

def access_restricted_function(account_address, private_key):
    # Build transaction to access restricted function
    nonce = w3.eth.get_transaction_count(account_address)
    tx = {
        'nonce': nonce,
        'to': CONTRACT_ADDRESS,
        'value': 0,
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'data': contract.encodeABI(fn_name='restrictedFunction', args=[])
    }
    
    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return tx_receipt

def perform_access_control_attack():
    # Attempt to access restricted function with user account
    user_address = get_account(USER_PRIVATE_KEY)
    print("Attempting with user account:")
    user_receipt = access_restricted_function(user_address, USER_PRIVATE_KEY)
    print("User transaction receipt:")
    print(user_receipt)

    # Attempt to access restricted function with admin account
    admin_address = get_account(ADMIN_PRIVATE_KEY)
    print("Attempting with admin account:")
    admin_receipt = access_restricted_function(admin_address, ADMIN_PRIVATE_KEY)
    print("Admin transaction receipt:")
    print(admin_receipt)

if __name__ == "__main__":
    perform_access_control_attack()

