## Intentionally Broken Flask Demo (For CI Failure Testing)

This repository is a **very small, intentionally broken** Python/Flask project.
It is designed **specifically to fail in CI** so you can test AI-powered or automated
log analysis tools.

### What this project contains

- **`app.py`** – Minimal Flask application with a deliberate runtime error.
- **`requirements.txt`** – Python dependencies (just Flask).
- **`.github/workflows/ci.yml`** – GitHub Actions workflow that runs on every push.
- **`README.md`** – This explanation.

### The intentional error

In `app.py` there is a clearly wrong import:

```python
import not_a_real_module  # <-- intentional broken import
```

This module **does not exist**, so any attempt to import `app` will immediately fail with:

```text
ModuleNotFoundError: No module named 'not_a_real_module'
```

Do **not** fix this if your goal is to have a consistently failing CI run.

### How the CI is set up to fail

The GitHub Actions workflow in `.github/workflows/ci.yml`:

1. Checks out the repository.
2. Sets up Python and installs `requirements.txt`.
3. Runs:

   ```bash
   python -c "import app"
   ```

Because of the bad import in `app.py`, this step **always fails**, and the CI job
is marked as failed. The traceback in the CI logs will clearly show the
`ModuleNotFoundError`, which is ideal for testing automated log analyzers.

### How to run locally (if you want to see the same failure)

```bash
pip install -r requirements.txt
python -c "import app"
```

You should see the same `ModuleNotFoundError` locally.

If you comment out or remove the bad import, the module will import successfully and
you can then run:

```bash
python app.py
```

to start the Flask development server. **But remember:** the whole point of this repo
is for CI to fail, so keep the broken import if you are using it for failure analysis.


