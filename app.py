from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the index page.
    """
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    """
    Example dynamic route.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Run locally for testing
    # Azure App Service will use 'gunicorn' in production
    app.run(host="0.0.0.0", port=5000, debug=True)
