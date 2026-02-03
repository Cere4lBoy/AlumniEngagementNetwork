from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

# =========================
# PATH SETUP
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "aens.db")

# =========================
# FLASK APP
# =========================

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)

# =========================
# DATABASE CONNECTION
# =========================

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# =========================
# REGISTER BLUEPRINTS
# =========================

# from .admin_routes import admin_bp
# from .officer_routes import officer_bp
# from .student_routes import student_bp

# app.register_blueprint(admin_bp)
# app.register_blueprint(officer_bp)
# app.register_blueprint(student_bp)

# =========================
# COMMON ROUTES
# =========================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Bypass authentication for now: always redirect to homepage after login
        # Original DB-based authentication commented out for reference:
        # email = request.form["email"]
        # password = request.form["password"]
        # conn = get_db_connection()
        # cursor = conn.cursor()
        # cursor.execute(
        #     "SELECT * FROM Users WHERE Email = ? AND Password = ?",
        #     (email, password)
        # )
        # user = cursor.fetchone()
        # conn.close()
        # if user:
        #     return redirect("/home")
        # else:
        #     return "Invalid login"
        return redirect("/home")

    return render_template("common/login.html")

@app.route("/home")
def home_page():
    return render_template("common/homepage.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # fullname = request.form["name"]
        # email = request.form["email"]
        # password = request.form["password"]
        # role = request.form["role"]

        # conn = get_db_connection()
        # cursor = conn.cursor()
        # cursor.execute(
        #     "INSERT INTO Users (FullName, Email, Password, Role) VALUES (?, ?, ?, ?)",
        #     (fullname, email, password, role)
        # )
        # conn.commit()
        # conn.close()

        return redirect("/login")

    return render_template("common/register.html")

@app.route("/notifications")
def notifications():
    return render_template("common/notifications.html")

@app.route("/about")
def about():
    return render_template("common/about.html")

@app.route("/logout")
def logout():
    return redirect(url_for("index"))

# =========================
# ALUMNI ROUTES
# =========================

@app.route("/alumni/dashboard")
def alumni_dashboard():
    return render_template("alumni/dashboard.html")

@app.route("/alumni/profile", methods=["GET", "POST"])
def alumni_profile():
    return render_template("alumni/profile.html")

@app.route("/alumni/career", methods=["GET", "POST"])
def alumni_career():
    return render_template("alumni/career.html")

@app.route("/alumni/testimonial", methods=["GET", "POST"])
def alumni_testimonial():
    return render_template("alumni/testimonial.html")

# =========================
# ADMIN ROUTES
# =========================

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/admin.html')

@app.route('/admin/users/approve')
def admin_approve_users():
    return render_template('admin/user_approval.html')

@app.route('/admin/users/suspend')
def admin_suspend_users():
    return render_template('admin/suspend_user.html')

@app.route('/admin/users/roles')
def admin_assign_roles():
    return render_template('admin/assign_roles.html')

@app.route('/admin/users/reset-password')
def admin_reset_password():
    return render_template('admin/reset_user_password.html')

@app.route('/admin/events/manage')
def admin_manage_events():
    return render_template('admin/event_management.html')

@app.route('/admin/events/announce')
def admin_publish_announcement():
    return render_template('admin/publish_announcement.html')

@app.route('/admin/testimonials')
def admin_manage_testimonials():
    return render_template('admin/testimonial_approval.html')

@app.route('/admin/system/notify')
def admin_send_notification():
    return render_template('admin/send_notification.html')

@app.route('/admin/system/settings')
def admin_system_settings():
    return render_template('admin/system_settings.html')

@app.route('/admin/events/create', methods=['GET', 'POST'])
def admin_create_event():
    if request.method == 'POST':
        return redirect('/admin/events/manage')
    return render_template('admin/event_create.html')

@app.route('/admin/events/edit', methods=['GET', 'POST'])
def admin_edit_event():
    if request.method == 'POST':
        return redirect('/admin/events/manage')
    return render_template('admin/edit_event.html')

@app.route('/admin/events/delete')
def admin_delete_event():
    return redirect('/admin/events/manage')

# =========================
# OFFICER ROUTES
# =========================

@app.route('/officer/dashboard')
def officer_dashboard():
    return render_template('officer/dashboard.html')

@app.route('/officer/jobs/create')
def officer_create_job():
    return render_template('officer/jobs/create_job.html')

@app.route('/officer/jobs/edit')
def officer_edit_job():
    return render_template('officer/jobs/edit_job.html')

@app.route('/officer/applications')
def officer_applications():
    return render_template('officer/applications.html')

@app.route('/officer/mentorship_review')
def officer_mentorship_review():
    return render_template('officer/mentorship_review.html')

@app.route('/officer/notifications')
def officer_notifications():
    return render_template('officer/notifications.html')

# =========================
# STUDENT ROUTES
# =========================

@app.route('/student/home')
def student_dashboard():
    return render_template('student/home.html')

@app.route('/student/feed')
def student_feed():
    return render_template('student/feed.html')

@app.route('/student/events')
def student_events():
    return render_template('student/events.html')

@app.route('/student/events/register')
def student_event_register():
    return render_template('student/event_register.html')

@app.route('/student/jobs')
def student_jobs():
    return render_template('student/jobs.html')

@app.route('/student/jobs/apply')
def student_job_apply():
    return render_template('student/job_apply.html')

@app.route('/student/mentorship')
def student_mentorship():
    return render_template('student/mentorship.html')

@app.route('/student/profile')
def student_profile():
    return render_template('student/profile.html')

@app.route('/student/notifications')
def student_notifications():
    return render_template('student/notifications.html')


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)
