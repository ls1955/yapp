# YAPP

Yet Another Python Project in the university.

## Getting Started

### Linux

1. Clone and navigate to this repo.
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `echo "export FLASK_APP='yapp'" >> ~/.bashrc`
6. `echo "export FLASK_ENV='development'" >> ~/.bashrc`
7. `source .bashrc`
8. `flask init-db`
9. `flask run --debug`
10. Visit `http://localhost:5000/`.

## TODOs

- Have something like `flask init-encyrption-keys`
- Automated scripts to measure performance and accuracy
