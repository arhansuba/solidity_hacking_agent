import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_to_cyberflood(script_path):
    """
    Imports data into Spirent CyberFlood using the specified script.

    Args:
        script_path (str): Path to the Spirent CyberFlood import script.

    Raises:
        FileNotFoundError: If the specified script does not exist.
        subprocess.CalledProcessError: If the subprocess fails.
    """
    script_path = Path(script_path)

    if not script_path.is_file():
        logging.error(f"Script file not found: {script_path}")
        raise FileNotFoundError(f"Script file not found: {script_path}")

    logging.info(f"Importing data using Spirent CyberFlood script: {script_path}")

    try:
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
        logging.info("Import completed successfully.")
        logging.debug(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error("Import failed.")
        logging.error(f"Error message:\n{e.stderr}")
        raise

if __name__ == "__main__":
    script_path = './spirent_import_script.py'
    import_to_cyberflood(script_path)
