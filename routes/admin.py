from flask import Blueprint, jsonify, session, render_template
from db import get_connection

admin_bp = Blueprint("admin", __name__)


# Admin dashboard
@admin_bp.route("/admin/dashboard")
def admin_dashboard():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "ADMIN":
        return jsonify({
            "success": False,
            "message": "Admin access required"
        }), 403

    return render_template(
        "admin/dashboard.html",
        username=session.get("username")
    )


# Get ERP statistics
@admin_bp.route("/admin/statistics")
def statistics():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "ADMIN":
        return jsonify({
            "success": False,
            "message": "Admin access required"
        }), 403

    connection = get_connection()
    cursor = connection.cursor()

    # Students
    cursor.execute("SELECT COUNT(*) FROM student")
    students = cursor.fetchone()[0]

    # Faculty
    cursor.execute("SELECT COUNT(*) FROM faculty")
    faculty = cursor.fetchone()[0]

    # Courses
    cursor.execute("SELECT COUNT(*) FROM course")
    courses = cursor.fetchone()[0]

    # Notices
    cursor.execute("SELECT COUNT(*) FROM notices")
    notices = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return jsonify({
        "success": True,
        "students": students,
        "faculty": faculty,
        "courses": courses,
        "notices": notices
    })