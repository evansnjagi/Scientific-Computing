# Scientific-Computing ✅

Welcome! This repository is a beginner-friendly collection of small examples for learning Python and basic algorithms. It focuses on a simple Caesar cipher implementation and includes clear instructions, tests, and exercises so you can learn by doing.

---

## 🔧 Getting started

### Prerequisites
- Python 3.11+ installed
- (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dev dependencies

```bash
pip install -r requirements-dev.txt
```

### Run an example

Encrypt a message from the command line:

```bash
python -m cipher.encryption encrypt "Hello, World!" -s 3
```

Decrypt a message:

```bash
python -m cipher.encryption decrypt "khoor, zruog" -s 3
```

Or run the demo:

```bash
python -m cipher.decryption
```

---

## ✅ What we improved for beginners
- Clear `encrypt` / `decrypt` functions with **docstrings** and **type hints**
- A small **CLI** for quick experimentation
- **Unit tests** (pytest) demonstrating expected behavior
- A friendly README with setup, usage, and exercises
- Guidance on contributions and learning next steps

---

## 🧪 Running tests

```bash
pytest -q
```

---

## 💡 Exercises for learners
1. Modify the cipher to support a custom alphabet (e.g., include digits).
2. Add support for ROT13 as a special case and write tests.
3. Create a GUI (Tkinter) that lets users type messages and see live encryption.

---

## Contributing
See `CONTRIBUTING.md` for how to contribute and run the test suite.

---

## License
This project is licensed under the MIT License — see `LICENSE`.
