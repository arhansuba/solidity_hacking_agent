import json
import subprocess
from typing import Any, Dict, List

def run_tests(contract_path: str) -> Dict[str, Any]:
    """Run various tests on the smart contract."""
    
    test_results = {}
    
    # Ensure myth is installed
    if subprocess.run(["which", "myth"], capture_output=True, text=True).returncode != 0:
        raise FileNotFoundError("The 'myth' command is not found. Please install it.")

    # Mythril analysis
    mythril_result = subprocess.run(
        ["myth", "analyze", contract_path],
        capture_output=True, text=True
    )
    test_results["mythril_analysis"] = {
        "stdout": mythril_result.stdout,
        "stderr": mythril_result.stderr,
        "returncode": mythril_result.returncode
    }

    return test_results

def comprehensive_testing(contract_path: str) -> Dict[str, Any]:
    """Perform comprehensive testing on the smart contract."""
    return run_tests(contract_path)

# Usage
contract_path = "/home/arhan/SolidityHackingAgent/MultiOwnable.sol"
try:
    test_results = comprehensive_testing(contract_path)
    print(test_results)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
