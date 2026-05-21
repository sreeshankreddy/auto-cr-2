# AI-Powered Automated Code Reviewer

## Overview
An intelligent system that automatically reviews source code to identify bugs, security vulnerabilities, performance issues, and code-quality problems, providing explanations and suggested fixes.

## Features
- **Multiple Input Methods:** Supports code pasting, file uploads, zip projects, and GitHub repository analysis.
- **Comprehensive Review:** Detects syntax errors, logical bugs, code smells, complexity issues, and security vulnerabilities.
- **AI-Powered Refactoring:** Uses LLMs to generate improved code, better naming, and documentation.
- **Security Scans:** Identifies SQL injection, hardcoded credentials, and unsafe API usage.
- **Report Generation:** Produces actionable reports for review findings.

## Folder Structure
- `app.py`: Main Streamlit interface.
- `utils/`: Core utilities (Parser, Reviewer, Security, GitHub, Reporting).
- `models/`: AI model integration.
- `database/`: SQLite database persistence.
- `tests/`: Automated test suite.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenAI API key in `.env`.
4. Run: `streamlit run app.py`

## Deployment
- **Docker:** Build using `docker build -t code-reviewer .` and run with `docker-compose up`.
- **Streamlit Cloud:** Connect the repository to your Streamlit Cloud account for automated deployment.

## Future Improvements
- Support for more programming languages.
- Integration with more CI/CD pipelines (GitLab, Bitbucket).
- Advanced AI models for specific security vulnerabilities.
