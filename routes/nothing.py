from flask import Flask, render_template, request, redirect, url_for
import os

import sqlite3


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "aens.db")

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows dict-like access
    return conn



# =========================
# COMMON ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM Users
            WHERE Email = ? AND Password = ?
        """, (email, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect("/home")
        else:
            return "Invalid login"

    return render_template("common/login.html")


@app.route("/home")
def home_page():
    return render_template("common/homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Users (FullName, Email, Password, Role)
            VALUES (?, ?, ?, ?)
        """, (fullname, email, password, role))

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("common/register.html")



@app.route("/notifications")
def notifications():
    return render_template("common/notifications.html")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))

@app.route("/user-selection", methods=["GET", "POST"])
def user_selection():
    if request.method == "POST":
        role = request.form.get("role")
        return redirect(url_for("register", role=role))
    return render_template("common/user_selection.html")



# =========================
# ALUMNI ROUTES
# =========================

@app.route("/alumni/dashboard")
def alumni_dashboard():
    return render_template("alumni/dashboard.html")


@app.route("/alumni/profile", methods=["GET", "POST"])
def alumni_profile():
    if request.method == "POST":
        print(request.form)
    return render_template("alumni/profile.html")


@app.route("/alumni/career", methods=["GET", "POST"])
def alumni_career():
    if request.method == "POST":
        print(request.form)
    return render_template("alumni/career.html")


@app.route("/alumni/testimonial", methods=["GET", "POST"])
def alumni_testimonial():
    if request.method == "POST":
        print(request.form)
    return render_template("alumni/testimonial.html")


if __name__ == "__main__":
    app.run(debug=True)
