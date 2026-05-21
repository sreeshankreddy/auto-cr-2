# Project Structure

code-reviewer/
├── app.py              # Main Streamlit application entry point
├── utils/              # Helper modules
│   ├── code_parser.py     # Detects language, extracts functions/classes
│   ├── code_cleaner.py    # Sanitizes code inputs
│   ├── reviewer.py        # Orchestrates the review workflow
│   ├── security_checker.py # Scans for security vulnerabilities
│   ├── github_fetcher.py  # Interacts with GitHub API
│   └── report_generator.py# Generates PDF/Summary reports
├── models/             # AI model logic
│   └── ai_reviewer.py     # LLM integration for deep analysis
├── database/           # Persistence layer
│   └── db.py              # SQLite interaction
├── reports/            # Storage for generated reports
├── tests/              # Unit and integration tests
├── docs/               # Documentation
└── requirements.txt    # Project dependencies

## Explanation:
- `app.py`: The heart of the application, managing the UI and routing user actions to backend services.
- `utils/`: Contains focused, reusable utility functions for specific parts of the pipeline, keeping the core application logic clean.
- `models/`: Separates AI-related logic from general utility logic.
- `database/`: Handles all data persistence, separating DB schema and queries from business logic.
- `reports/`: A dedicated folder to store generated analysis reports.
- `tests/`: A folder for tests to ensure code quality and system reliability.
- `docs/`: Stores project documentation, including the design document.
