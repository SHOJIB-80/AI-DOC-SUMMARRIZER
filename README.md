# AI Document Summarizer

This project is a Python-based command-line tool for summarizing long text input. It collects document text from the terminal, sends the text to a summarization agent, and prints a concise summary back to the console. When a valid Gemini API key is configured, the project uses the Gemini API; otherwise, it falls back to a local summarization routine.

## Kaggle Writeup

- https://kaggle.com/competitions/agents-intensive-capstone-project/writeups/ai-doc-summarizer

## Overview

The application is built as a simple terminal workflow rather than a web app or service. A user starts the script, enters a document line by line, and ends input with `END`. The application then creates a prompt and passes it to the summarization agent. The agent attempts to use Gemini if available, and if the model call fails or returns no result, it uses a local summarizer as a fallback.

This repository is a lightweight proof-of-concept for AI-assisted document summarization and is focused on the summarization flow rather than deployment, authentication, or database-backed storage.

## Features

- Terminal input for document text
- Prompt-based summarization workflow
- Gemini API integration when configured
- Local fallback summarization when the API is unavailable
- Simple console output for generated summaries

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| google-generativeai | Gemini API client library |
| Gemini 1.5 Flash | LLM used for summarization |
| Standard input/output | User interaction in the terminal |

## Project Structure

```text
AI-DOC-SUMMARRIZER/
├── .gitignore
├── README.md
├── about.pdf
├── agent.py
├── api.env
├── main.py
├── memory_bank.py
├── requirements.txt
├── session.py
├── tools.py
├── utils.py
└── __pycache__/
```

### Important files

- `main.py` launches the document input loop and runs the summarizer.
- `agent.py` defines `DocumentSummarizerAgent`, which builds the prompt and handles the model fallback.
- `utils.py` configures the Gemini client and calls the model.
- `requirements.txt` contains the project dependency.
- `api.env` exists in the repository but is currently empty.
- `memory_bank.py`, `session.py`, and `tools.py` are present in the repository but do not currently contain a working implementation.

## System Architecture

```text
User
  ↓
Terminal input
  ↓
main.py
  ↓
DocumentSummarizerAgent
  ↓
Gemini API / fallback summarizer
  ↓
Console output
```

The system is intentionally simple: the user provides text, the Python script calls the agent, and the final summary is displayed in the terminal.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SHOJIB-80/AI-DOC-SUMMARRIZER.git
cd AI-DOC-SUMMARRIZER
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The project currently configures the Gemini client directly in `utils.py`:

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")
```

A valid Gemini API key must be added in place of the placeholder before the model-based summarization path can work. The repository also contains `api.env`, but it is empty and is not wired into the application code.

## Running the Project

Run the application with:

```bash
python main.py
```

Then paste the document text to summarize. Finish the input with:

```text
END
```

The program prints the generated summary in the terminal.

## Application Usage

1. Start the script.
2. Enter the document content line by line.
3. Type `END` when the document is complete.
4. Review the generated summary in the terminal.

This project does not include a graphical interface or a multi-user web workflow.

## Authentication and Authorization

This project does not implement authentication, user accounts, role-based access control, or protected routes. There is no login flow or session management system in the current repository.

## Testing

No automated tests are present in the repository. There are no test scripts, test files, or CI configuration related to validation.

## Known Limitations

- The project is a lightweight terminal prototype rather than a production-ready application.
- The Gemini API key must be set manually in `utils.py`.
- `memory_bank.py`, `session.py`, and `tools.py` are present as repository files but do not currently contain complete implementations.
- There is no database, backend API, or web interface.
- There is no license file in the repository.

## Security Considerations

The code does not implement a secure user authentication system, encrypted storage, or protected API infrastructure. The application uses an API key directly in code, which means the key must be managed carefully by the developer and should not be committed in a real environment.

## License

No license file is present in the repository, so the project does not currently declare a license.

## Author

No author metadata is included in the repository files.

## Summary

This project provides a simple Python-based document summarization workflow that can generate concise summaries from user input. It uses Gemini when configured and falls back to a built-in summarizer if the model is unavailable. The repository is intentionally minimal and focused on the summarization flow rather than a broader application architecture.
