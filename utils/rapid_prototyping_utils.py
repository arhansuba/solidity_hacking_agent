# rapid_prototyping_utils.py

import tempfile

def create_temp_file(content: str) -> str:
    """
    Create a temporary file with the given content.
    """
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write(content)
        return temp_file.name

def load_temp_file(file_path: str) -> str:
    """
    Load the content of a temporary file.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content
