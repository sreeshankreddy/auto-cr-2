import re

def check_security(code):
    """
    Scans code for common security vulnerabilities using regex patterns.
    """
    vulnerabilities = []
    
    # 1. Hardcoded Credentials
    if re.search(r'(password|passwd|pwd|api_key|secret)\s*=\s*["\'][^"\']+["\']', code, re.IGNORECASE):
        vulnerabilities.append({
            "type": "Hardcoded Credentials",
            "severity": "Critical",
            "description": "Found potential hardcoded secret or password."
        })
    
    # 2. SQL Injection Risk
    if re.search(r'SELECT.*FROM.*WHERE.*=', code, re.IGNORECASE) and '+' in code:
         vulnerabilities.append({
            "type": "SQL Injection",
            "severity": "Critical",
            "description": "Found potential SQL concatenation. Use parameterized queries."
        })

    # 3. Unsafe file operations
    if re.search(r'open\(.*input\(', code):
        vulnerabilities.append({
            "type": "Unsafe File Operation",
            "severity": "High",
            "description": "Found potential unsafe file opening using user input."
        })
        
    return vulnerabilities
