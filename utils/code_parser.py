import os
import mimetypes

def detect_language(file_path):
    """
    Detects the programming language based on file extension.
    """
    ext = os.path.splitext(file_path)[1]
    mapping = {
        '.py': 'Python',
        '.java': 'Java',
        '.js': 'JavaScript',
        '.c': 'C',
        '.cpp': 'C++',
        '.sql': 'SQL',
        '.go': 'Go',
        '.html': 'HTML',
        '.css': 'CSS'
    }
    return mapping.get(ext, 'Unknown')

def read_file_content(file_path):
    """
    Reads the content of a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def extract_code_structure(code, language):
    """
    Basic extraction of functions/classes based on language.
    This can be expanded with tree-sitter or regex for more accuracy.
    """
    # Simple regex-based approach for demonstration
    if language == 'Python':
        import re
        classes = re.findall(r'class\s+(\w+)', code)
        functions = re.findall(r'def\s+(\w+)', code)
        return {"classes": classes, "functions": functions}
    return {"classes": [], "functions": []}
