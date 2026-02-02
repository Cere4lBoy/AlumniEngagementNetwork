from flask import Blueprint, render_template

officer_bp = Blueprint("officer_bp", __name__, url_prefix="/officer")

@officer_bp.route("/dashboard")
def dashboard():
    return render_template("officer/dashboard.html")


@officer_bp.route("/jobs/create_job")
def create_job():
    return render_template("officer/jobs/create_job.html")


@officer_bp.route("/jobs/edit_job")
def edit_job():
    return render_template("officer/jobs/edit_job.html")


@officer_bp.route("/applications")
def applications():
    return render_template("officer/applications.html")


@officer_bp.route("/mentorship_review")
def mentorship_review():
    return render_template("officer/mentorship_review.html")


@officer_bp.route("/notifications")
def notifications():
    return render_template("officer/notifications.html")
