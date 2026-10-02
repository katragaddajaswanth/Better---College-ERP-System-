from flask import Blueprint, request, jsonify, render_template
from db import get_connection

attendance_bp = Blueprint("attendance", __name__)


# Attendance page
@attendance_bp.route("/attendance")
def attendance_page():
    return render_template("public/attendance.html")


# Attendance API
@attendance_bp.route("/api/attendance", methods=["POST"])
def get_attendance():

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
            a.attended_classes,
            a.total_classes
        FROM attendance a
        JOIN student s
            ON a.student_id = s.student_id
        JOIN course c
            ON a.course_id = c.course_id
        WHERE a.student_id = :student_id
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
            "message": "No attendance records found"
        })

    attendance = []

    for row in rows:

        student_name = row[0]
        course_name = row[1]
        attended = row[2]
        total = row[3]

        if total > 0:
            percentage = (attended / total) * 100
        else:
            percentage = 0

        attendance.append({
            "student_name": student_name,
            "course": course_name,
            "attended": attended,
            "total": total,
            "percentage": round(percentage, 2)
        })

    return jsonify({
        "success": True,
        "attendance": attendance
    })