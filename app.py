from flask import Flask

# Intentional error for CI demo:
# This import does NOT exist and will raise:
# ModuleNotFoundError: No module named 'not_a_real_module'
import not_a_real_module  # noqa: F401  # <-- intentional broken import


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from the intentionally broken demo app!"


if __name__ == "__main__":
    # In normal code we would run the app here.
    # The broken import above prevents this file from running successfully.
    app.run(host="0.0.0.0", port=5000, debug=True)


