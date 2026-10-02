from flask import Blueprint, request, jsonify, render_template
from db import get_connection

results_bp = Blueprint("results", __name__)


# Results page
@results_bp.route("/results")
def results_page():
    return render_template("public/results.html")


# Results API
@results_bp.route("/api/results", methods=["POST"])
def get_results():

    data = request.get_json()

    student_id = data.get("student_id")

    if not student_id:
        return jsonify({
            "success": False,
            "message": "Student ID is required"
        })

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks,
            r.grade,
            r.result_status
        FROM results r
        JOIN student s
            ON r.student_id = s.student_id
        JOIN course c
            ON r.course_id = c.course_id
        WHERE r.student_id = :student_id
        ORDER BY c.course_id
    """

    cursor.execute(
        query,
        student_id=student_id
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    if not rows:
        return jsonify({
            "success": False,
            "message": "No result records found"
        })

    results = []

    for row in rows:

        results.append({
            "student_name": row[0],
            "course": row[1],
            "marks": float(row[2]),
            "grade": row[3],
            "status": row[4]
        })

    return jsonify({
        "success": True,
        "results": results
    })