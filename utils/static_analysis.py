import subprocess
import json
import tempfile
import os

def run_static_analysis(code_content, language):
    """
    Runs static analysis tools based on the language.
    """
    if language != 'Python':
        return {"error": "Static analysis currently only supports Python."}

    # Create a temporary file for analysis
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp:
        tmp.write(code_content)
        tmp_path = tmp.name

    results = {
        "pylint": run_pylint(tmp_path),
        "bandit": run_bandit(tmp_path),
        "radon": run_radon(tmp_path)
    }

    os.remove(tmp_path)
    return results

def run_pylint(file_path):
    """Runs pylint and returns issues."""
    try:
        # Using json output for easier parsing
        cmd = ["pylint", "--output-format=json", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else []
    except Exception as e:
        return {"error": str(e)}

def run_bandit(file_path):
    """Runs bandit for security issues."""
    try:
        cmd = ["bandit", "-f", "json", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else {}
    except Exception as e:
        return {"error": str(e)}

def run_radon(file_path):
    """Runs radon for cyclomatic complexity."""
    try:
        cmd = ["radon", "cc", file_path, "-j"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else {}
    except Exception as e:
        return {"error": str(e)}
