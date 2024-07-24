import re
from pylint import lint
from pylint.reporters.text import TextReporter
from io import StringIO

def check_code_cleanliness(contract_path):
    # Create a new pylint lint.Run instance
    pylint_output = StringIO()
    reporter = TextReporter(pylint_output)
    lint.Run([contract_path], reporter=reporter, exit=False)
    
    pylint_stdout = pylint_output.getvalue()
    pylint_stderr = None  # Pylint does not provide a direct way to capture stderr output

    # Extract pylint score
    score_match = re.search(r"Your code has been rated at (\d+\.\d+)/10", pylint_stdout)
    if score_match:
        pylint_score = float(score_match.group(1))
    else:
        pylint_score = 0.0
    
    # Check for common code smells
    with open(contract_path, 'r') as file:
        content = file.read()
        
    smells = {
        "long_functions": len(re.findall(r"function\s+\w+\s*\([^)]*\)\s*{[^}]{200,}", content)),
        "magic_numbers": len(re.findall(r"\b\d+\b(?!\s*[;:=])", content)),
        "commented_code": len(re.findall(r"(\/\/.*|\*(.*\n)+?\*\/)\s*\w+\s*[\({]", content))
    }
    
    return {
        "pylint_score": pylint_score,
        "code_smells": smells
    }

# Usage example
if __name__ == "__main__":
    contract_path = "/home/arhan/SolidityHackingAgent/MultiOwnable.sol"
    cleanliness_report = check_code_cleanliness(contract_path)
    print(cleanliness_report)
