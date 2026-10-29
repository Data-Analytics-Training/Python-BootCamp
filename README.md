# Python Bootcamp

[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An eight-week, hands-on bootcamp repository that takes learners from Python syntax
fundamentals through web development, data processing, and visualization. This is
not a single application; it contains standalone lesson examples, Jupyter notebooks,
practice exercises, and sample data files.

## Overview

- **Duration:** 8 weeks, 24 lessons/sections
- **Target audience:** Python beginners and learners strengthening their fundamentals
- **Python:** `>=3.14` (pinned by `.python-version`)
- **Educational content:** 295 Python examples and 13 Jupyter notebooks
- **Package management:** `uv` and `uv.lock`
- **License:** MIT

## Curriculum

| Week | Content | Main tools | Content count |
|---|---|---|---:|
| **01** | Python fundamentals: syntax, variables, types, input, and conditionals | Python standard library | 59 Python files |
| **02** | Control flow, lists, loops, functions, strings, and errors | Python standard library | 67 Python files |
| **03** | File operations, text, JSON, and CSV | `json`, `csv`, `datetime`, `os` | 45 Python files |
| **04** | Databases and ORM | SQLite, SQLAlchemy, DuckDB | 55 Python files |
| **05** | HTTP clients and web scraping | Requests, HTTPX, BeautifulSoup, Selenium, Playwright | 40 Python files |
| **06** | Web applications and APIs | Flask, FastAPI, Jinja2, Uvicorn | 21 Python files |
| **07** | NumPy and array operations | NumPy, Jupyter | 3 notebooks |
| **08** | Data frames and visualization | Pandas, Polars, Matplotlib, Plotly, Seaborn | 6 notebooks |

The `Practice/` directory also contains 8 Python exercises and 4 interactive
notebooks. File counts refer to educational content; the package skeleton under
`src/python_bootcamp/` is not included.

## Directory Structure

```text
Python-BootCamp/
├── Week01/                         # Python fundamentals
├── Week02/                         # Control flow and functions
├── Week03/                         # File, JSON, and CSV operations
├── Week04/                         # SQLite, SQLAlchemy, and DuckDB
├── Week05/                         # HTTP, scraping, and browser automation
├── Week06/                         # Flask and FastAPI examples
├── Week07/                         # NumPy notebooks
├── Week08/                         # Pandas, Polars, and visualization
├── Practice/                       # Exercises and notebooks
├── src/python_bootcamp/            # Package entry-point skeleton
├── pyproject.toml                  # Project and dependency definitions
├── uv.lock                         # Locked dependency versions
└── LICENSE
```

The week directories contain lesson folders with their original date-based names.
For example, `Week05/Lesson14 - 2025.10.15/` contains HTTPX and BeautifulSoup
examples, while `Week06/Lesson18 - 2025.10.25/` contains Flask, database, and API
examples.

## Installation

### Recommended: uv

If [uv](https://docs.astral.sh/uv/) is not installed, follow the installation
instructions for your operating system in the official documentation. Then run:

```bash
git clone https://github.com/onurdoker/Python-BootCamp.git
cd Python-BootCamp

# Creates a virtual environment and installs the locked dependencies with Python 3.14
uv sync
```

`uv sync` installs the runtime and development dependencies defined in
`pyproject.toml`. Activating the environment is not required; commands can be
run directly with `uv run`.

### Alternative: venv + pip

```bash
python3.14 -m venv .venv
source .venv/bin/activate          # macOS/Linux
# Windows:
# .venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install jupyterlab pytest ruff
```

The `example02` and `example03` applications under `Week06/Lesson18` use
Flask-SQLAlchemy. This dependency is not currently listed in the project
manifest, so install it separately before running those examples:

```bash
uv pip install flask-sqlalchemy
# or, inside an active virtual environment:
python -m pip install flask-sqlalchemy
```

## Quick Start

### Run a Python example

Examples are run as standalone files:

```bash
uv run python "Week01/Lesson01 - 2025.09.15/example01.py"
uv run python "Week05/Lesson14 - 2025.10.15/httpx/example02.py"
```

If you are not using `uv`, replace `uv run python` with `python` while the virtual
environment is active.

### Package entry point

The project also defines a `python-bootcamp` command:

```bash
uv run python-bootcamp
```

At present, this command only prints a greeting to verify that the package skeleton
is working; it does not launch a particular lesson or web application.

### Start Jupyter

```bash
uv run jupyter lab
```

Then open a notebook under `Practice/`, `Week07/`, or `Week08/`. To open only the
Practice directory:

```bash
uv run jupyter lab Practice/
```

### Run Flask and FastAPI examples

Each application should be started from its own lesson directory. For example:

```bash
cd "Week06/Lesson16 - 2025.10.20/Flask/example01"
uv run python app.py
```

The port used by FastAPI examples varies; check the `uvicorn.run(...)` line in the
file. Flask examples usually use port `5000`, while FastAPI examples commonly use
port `5001` or `8000`. These lesson examples are educational and generally run in
debug mode; they should not be used in production.

### Playwright and Selenium

Install the Playwright browser binaries before running Playwright examples:

```bash
uv run playwright install
```

Selenium examples require a local browser and a compatible WebDriver. Some examples
use `webdriver-manager`, while others use the local `chromedriver` file in the
lesson directory. Behavior may vary depending on the operating system, browser
version, and file permissions.

## External Services and Safe Usage

Some web scraping and API examples connect to publicly accessible services on the
internet. Results may change because of network availability, changes to a remote
site's HTML, rate limits, or service changes.

- Respect each site's terms of service and `robots.txt` rules.
- Use reasonable request intervals and do not attempt to collect authenticated
  content without permission.
- Treat hard-coded passwords, secrets, and local network addresses in lessons as
  demo data only; never use them in real projects.
- Some requests under `Week06/Lesson18 - 2025.10.25/example04/api_request_files/`
  target the local address `192.168.1.12` and will not work unchanged in most
  environments.

## Practice Content

The `Practice/` directory contains:

- `Section01.ipynb` - `Section04.ipynb`: fundamentals and interactive exercises
- `Section05-Q*.py`: function, string, and problem-solving exercises
- `Section06-Q*.py`: data structure and algorithm exercises

Some historical naming differences remain in the filenames; for example,
`Section5-Q4.py` does not follow the `Section05-Q4.py` format.

## Testing and Code Quality

`pytest` and `ruff` are defined as development dependencies, but the project
currently has no separate test directory or automated CI configuration. Run the
basic checks with:

```bash
uv run pytest
uv run ruff check .
```

Because there are currently no test files, `pytest` may complete without collecting
tests. Validate notebooks and live web examples by running the relevant notebook or
example directly.

## Contributing

Pull requests are welcome for improving educational examples, correcting explanations,
or adding new practice exercises. When adding an example:

1. Follow the naming style used by the relevant week and lesson directory.
2. Document external services or special system requirements clearly.
3. Update the run instructions and required dependencies.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🐍
