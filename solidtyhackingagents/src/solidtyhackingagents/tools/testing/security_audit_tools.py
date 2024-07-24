# security_audit_tools.py

import subprocess

class SecurityAuditTools:
    def __init__(self):
        self.tools = {
            "nmap": "nmap -sP localhost",
            "nikto": "nikto -host localhost",
            "bandit": "bandit -r ."
        }

    def run_tool(self, tool_name: str):
        """
        Run a security audit tool.
        """
        command = self.tools.get(tool_name)
        if not command:
            print(f"Tool {tool_name} not found.")
            return

        print(f"Running {tool_name}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

# Example usage
if __name__ == "__main__":
    audit_tools = SecurityAuditTools()
    audit_tools.run_tool("nmap")
    audit_tools.run_tool("nikto")
    audit_tools.run_tool("bandit")
