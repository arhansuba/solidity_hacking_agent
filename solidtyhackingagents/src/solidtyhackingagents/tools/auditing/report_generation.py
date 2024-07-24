import json
import subprocess
import os
from typing import Any, Dict, List

def run_retests(contract_path: str, vulnerabilities: List[str]) -> Dict[str, Any]:
    """Retest the smart contract for previously identified vulnerabilities."""
    
    retest_results = {}
    
    if not os.path.isfile(contract_path):
        retest_results["error"] = f"Contract file not found at: {contract_path}"
        return retest_results

    for vulnerability in vulnerabilities:
        if vulnerability == "integer_underflow":
            result = subprocess.run(["myth", "analyze", "--execution-timeout", "300", contract_path, "-s", "integer_underflow"], capture_output=True, text=True)
            retest_results["integer_underflow"] = result.stdout
        
        elif vulnerability == "reentrancy":
            result = subprocess.run(["myth", "analyze", "--execution-timeout", "300", contract_path, "-s", "reentrancy"], capture_output=True, text=True)
            retest_results["reentrancy"] = result.stdout
        
        # Add other vulnerabilities and corresponding retest commands as needed
    
    return retest_results

def retest_verification(contract_path: str, initial_report_path: str) -> Dict[str, Any]:
    """Perform retesting verification on the smart contract."""
    
    if not os.path.isfile(initial_report_path):
        return {"error": f"Initial report file not found at: {initial_report_path}"}
    
    # Load initial report
    with open(initial_report_path, 'r') as file:
        initial_report = json.load(file)
    
    vulnerabilities = initial_report.get("identified_vulnerabilities", [])
    
    retest_results = run_retests(contract_path, vulnerabilities)
    
    # Save retest results to file
    with open("retest_results.json", 'w') as file:
        json.dump(retest_results, file, indent=4)
    
    return retest_results

# Usage
contract_path = "/home/arhan/SolidityHackingAgent/MultiOwnable.sol"  # Update this path when the contract is available
initial_report_path = "/home/arhan/SolidityHackingAgent/security_report.json"
retest_results = retest_verification(contract_path, initial_report_path)
print(retest_results)
