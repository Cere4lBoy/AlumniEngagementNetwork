from flask import Flask
from routes.officer_routes import officer_bp

app = Flask(__name__)

# Register officer routes
app.register_blueprint(officer_bp)

@app.route("/")
def home():
    return """
    <h2>AENS Flask is running ✅</h2>
    <p>Go to <a href="/officer/dashboard">/officer/dashboard</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
