from flask import Blueprint, jsonify, session, render_template
from db import get_connection

faculty_bp = Blueprint("faculty", __name__)


# Faculty dashboard
@faculty_bp.route("/faculty/dashboard")
def faculty_dashboard():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "FACULTY":
        return jsonify({
            "success": False,
            "message": "Faculty access required"
        }), 403

    return render_template(
        "faculty/dashboard.html",
        username=session.get("username")
    )


# Faculty profile
@faculty_bp.route("/faculty/profile")
def faculty_profile():

    if "username" not in session:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    if session.get("role") != "FACULTY":
        return jsonify({
            "success": False,
            "message": "Faculty access required"
        }), 403

    username = session.get("username")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            f.faculty_id,
            f.faculty_name,
            f.email,
            d.department_name
        FROM faculty f
        JOIN department d
            ON f.department_id = d.department_id
        WHERE f.faculty_id = :faculty_id
    """

    cursor.execute(
        query,
        faculty_id=username
    )

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if not row:
        return jsonify({
            "success": False,
            "message": "Faculty profile not found"
        }), 404

    return jsonify({
        "success": True,
        "faculty_id": row[0],
        "faculty_name": row[1],
        "email": row[2],
        "department": row[3]
    })