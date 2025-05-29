# Proposal Bot

An automated proposal generation and management system.

## Features

- TBD

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd proposal-bot
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .[dev]
```

## Development

### Code Style
This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for code linting

To format code:
```bash
black .
isort .
```

### Testing
Run tests with:
```bash
pytest
```

With coverage:
```bash
pytest --cov=src tests/
```

## License

[Your chosen license]
