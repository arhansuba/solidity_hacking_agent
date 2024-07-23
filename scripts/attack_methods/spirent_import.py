import subprocess

# Function to import data into Spirent CyberFlood
def import_to_cyberflood(script_path):
    try:
        print(f"Importing data using Spirent CyberFlood script: {script_path}")
        subprocess.run(['python', script_path], check=True)
        print("Import completed.")
    except Exception as e:
        print("Import failed:", e)

# Example usage
if __name__ == "__main__":
    script_path = './spirent_import_script.py'
    import_to_cyberflood(script_path)
