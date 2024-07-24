import json
import os
import subprocess
from typing import Any, Dict, List

def run_retests(contract_path: str, vulnerabilities: List[str]) -> Dict[str, Any]:
    """Retest the smart contract for previously identified vulnerabilities."""
    
    retest_results = {}
    
    for vulnerability in vulnerabilities:
        if vulnerability == "integer_underflow":
            result = subprocess.run(
                ["myth", "analyze", "--execution-timeout", "300", contract_path, "-s", "integer_underflow"],
                capture_output=True, text=True
            )
            retest_results["integer_underflow"] = {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        
        elif vulnerability == "reentrancy":
            result = subprocess.run(
                ["myth", "analyze", "--execution-timeout", "300", contract_path, "-s", "reentrancy"],
                capture_output=True, text=True
            )
            retest_results["reentrancy"] = {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        
        # Add other vulnerabilities and corresponding retest commands as needed
    
    return retest_results

def retest_verification(contract_path: str, initial_report_path: str) -> Dict[str, Any]:
    """Perform retesting verification on the smart contract."""
    
    # Load initial report
    if not os.path.isfile(initial_report_path):
        raise FileNotFoundError(f"Initial report file not found: {initial_report_path}")
    
    with open(initial_report_path, 'r') as file:
        initial_report = json.load(file)
    
    vulnerabilities = initial_report.get("identified_vulnerabilities", [])
    
    if not vulnerabilities:
        raise ValueError("No vulnerabilities found in the initial report.")
    
    retest_results = run_retests(contract_path, vulnerabilities)
    
    # Save retest results to file
    with open("retest_results.json", 'w') as file:
        json.dump(retest_results, file, indent=4)
    
    return retest_results

# Usage
contract_path = "MultiOwnable.sol"
initial_report_path = "/home/arhan/SolidityHackingAgent/security_report.json"

try:
    retest_results = retest_verification(contract_path, initial_report_path)
    print(retest_results)
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
