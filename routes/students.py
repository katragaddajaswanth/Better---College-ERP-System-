from flask import Blueprint, jsonify, session, render_template
from db import get_connection

student_bp = Blueprint("student", __name__)


# Student dashboard
@student_bp.route("/student/dashboard")
def student_dashboard():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "STUDENT":
        return jsonify({
            "success": False,
            "message": "Student access required"
        }), 403

    return render_template(
        "student/dashboard.html",
        username=session.get("username")
    )


# Student profile
@student_bp.route("/student/profile")
def student_profile():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "STUDENT":
        return jsonify({
            "success": False,
            "message": "Student access required"
        }), 403

    student_id = session.get("student_id")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            s.student_id,
            s.student_name,
            s.email,
            s.phone,
            d.department_name,
            s.semester
        FROM student s
        JOIN department d
            ON s.department_id = d.department_id
        WHERE s.student_id = :student_id
    """

    cursor.execute(
        query,
        student_id=student_id
    )

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if not row:
        return jsonify({
            "success": False,
            "message": "Student profile not found"
        }), 404

    return jsonify({
        "success": True,
        "student_id": row[0],
        "student_name": row[1],
        "email": row[2],
        "phone": row[3],
        "department": row[4],
        "semester": row[5]
    })