import json
from datetime import datetime
from typing import Dict, Any, List
import subprocess

# Configuration
CONTRACT_PATH = 'path/to/smart_contract.sol'
REPORT_PATH = 'path/to/security_report.json'
OUTPUT_REPORT = 'path/to/generated_report.md'

def load_report(report_path: str) -> Dict[str, Any]:
    """Load the security report from file."""
    try:
        with open(report_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"last_checked": None, "issues": {}}

def run_pylint(contract_path: str) -> str:
    """Run pylint to check code cleanliness."""
    (pylint_stdout, pylint_stderr) = subprocess.Popen(["pylint", contract_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()
    return pylint_stdout

def run_mythril(contract_path: str) -> str:
    """Run Mythril to check for vulnerabilities."""
    result = subprocess.run(["myth", "analyze", contract_path], capture_output=True, text=True)
    return result.stdout

def run_slither(contract_path: str) -> str:
    """Run Slither to check for vulnerabilities."""
    result = subprocess.run(["slither", contract_path], capture_output=True, text=True)
    return result.stdout

def generate_report(report: Dict[str, Any], output_path: str):
    """Generate a structured report in Markdown format."""
    with open(output_path, 'w') as file:
        file.write("# Security Report\n")
        file.write(f"**Generated on:** {datetime.now().isoformat()}\n\n")
        
        file.write("## Summary\n")
        file.write(f"**Last Checked:** {report['last_checked']}\n\n")
        
        file.write("## Code Cleanliness\n")
        file.write("### Pylint Report\n")
        file.write("```\n")
        file.write(run_pylint(CONTRACT_PATH))
        file.write("```\n\n")
        
        file.write("## Vulnerability Analysis\n")
        file.write("### Mythril Report\n")
        file.write("```\n")
        file.write(run_mythril(CONTRACT_PATH))
        file.write("```\n\n")
        
        file.write("### Slither Report\n")
        file.write("```\n")
        file.write(run_slither(CONTRACT_PATH))
        file.write("```\n\n")
        
        file.write("## Detailed Issues\n")
        for issue_type, issues in report['issues'].items():
            file.write(f"### {issue_type.capitalize()}\n")
            for issue in issues:
                file.write(f"- {issue}\n")
            file.write("\n")

def generate_security_report():
    """Main function to generate the security report."""
    report = load_report(REPORT_PATH)
    
    # Gather additional data (if needed)
    pylint_report = run_pylint(CONTRACT_PATH)
    mythril_report = run_mythril(CONTRACT_PATH)
    slither_report = run_slither(CONTRACT_PATH)
    
    # Update report with gathered data
    report['pylint_report'] = pylint_report
    report['mythril_report'] = mythril_report
    report['slither_report'] = slither_report
    
    # Generate the final report
    generate_report(report, OUTPUT_REPORT)
    print(f"Report generated: {OUTPUT_REPORT}")

if __name__ == "__main__":
    generate_security_report()
