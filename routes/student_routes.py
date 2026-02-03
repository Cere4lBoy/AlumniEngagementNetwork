from flask import Blueprint, render_template

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/student"
)

# =====================
# STUDENT DASHBOARD
# =====================

@student_bp.route("/student/home")
def dashboard():
    return render_template("student/home.html")

# =====================
# SOCIAL FEED
# =====================

@student_bp.route("/feed")
def feed():
    return render_template("student/feed.html")

# =====================
# EVENTS
# =====================

@student_bp.route("/events")
def events():
    return render_template("student/events.html")

@student_bp.route("/events/register")
def event_register():
    return render_template("student/event_register.html")

# =====================
# JOB BOARD
# =====================

@student_bp.route("/jobs")
def jobs():
    return render_template("student/jobs.html")

@student_bp.route("/jobs/apply")
def job_apply():
    return render_template("student/job_apply.html")

# =====================
# MENTORSHIP
# =====================

@student_bp.route("/mentorship")
def mentorship():
    return render_template("student/mentorship.html")

# =====================
# PROFILE
# =====================

@student_bp.route("/profile")
def profile():
    return render_template("student/profile.html")

# =====================
# NOTIFICATIONS
# =====================

@student_bp.route("/notifications")
def notifications():
    return render_template("student/notifications.html")
