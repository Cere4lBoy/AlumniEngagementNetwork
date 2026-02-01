from flask import Flask, render_template

app = Flask(__name__)


#IMAN'S
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student():
    return render_template("/Dashboard/student.html")

@app.route("/alumni")
def alumni():
    return render_template("/Dashboard/alumni.html")

@app.route("/officer")
def officer():
    return render_template("/Dashboard/officer.html")

@app.route("/admin")
def admin():
    return render_template("/Dashboard/admin.html")



#nono touch
if __name__ == "__main__":
    app.run(debug=True)
