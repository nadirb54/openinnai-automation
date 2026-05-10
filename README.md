# Open Innovation AI — Test Automation Framework

Playwright + Python test automation framework for Open Innovation AI.

---

## Prerequisites

- Python 3.10+
- pip
- [Allure CLI](https://allurereport.org/docs/install/) (for reports)

---

## Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd openinnai
```

### 2. Create and activate virtual environment

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

### 5. Add the .env file in the root directory

---

## Running Tests

### Run all tests (parallel, headless)

```bash
pytest
```

### Run all tests in headed mode (visible browser)

```bash
pytest --headed
```

### Run a specific test

```bash
pytest -k "test_request_demo"
```

### Run without parallelism (useful for debugging)

```bash
pytest -p no:xdist -s
```

### Run with a specific browser

```bash
pytest --browser=firefox
pytest --browser=webkit
pytest --browser=chromium  # default
```

### Run with a specific resolution

```bash
pytest --resolution=desktop  # default
pytest --resolution=tablet
pytest --resolution=phone
```

---

## Test Reports (Allure)

Reports are automatically generated in `reports/allure-results` after each run.

### Install Allure CLI

**Mac**
```bash
brew install allure
```

**Windows**
```bash
scoop install allure
```

**Linux**
```bash
sudo apt-get install allure
```

### Open the report

```bash
allure serve reports/allure-results
```

This will open an interactive HTML report in your browser.

---

## Project Structure

```
openinnai/
├── pages/                  # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py        # Base class for all pages
│   ├── xx_page.py
│   ├── yy_page.py
│   └── zz_page.py
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_assessement.py
├── reports/                # Generated test reports (gitignored)
├── .env                    # Environment variables (gitignored)
├── .gitignore
├── conftest.py             # Pytest fixtures and configuration
├── pytest.ini              # Pytest settings
└── requirements.txt        # Python dependencies
```

---

## Configuration

| Option | Default | Choices |
|---|---|---|
| `--browser` | `chromium` | `chromium`, `firefox`, `webkit` |
| `--resolution` | `desktop` | `desktop`, `tablet`, `phone` |
| `--headed` | headless | — |
| `-n` | `auto` | any number or `auto` |

---

## Troubleshooting

**Tests not found**
Make sure you are running `pytest` from the root of the project, not from inside the `tests/` folder.

**Module not found errors**
Make sure your virtual environment is activated — you should see `(venv)` in your terminal.

**Allure command not found**
Install Allure CLI following the instructions above for your OS.

**Browser not launching**
Run `playwright install` to make sure all browsers are installed.
