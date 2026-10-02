from flask import Blueprint, request, jsonify, render_template
from db import get_connection

fees_bp = Blueprint("fees", __name__)


# Fees page
@fees_bp.route("/fees")
def fees_page():
    return render_template("public/fees.html")


# Fee details API
@fees_bp.route("/api/fees", methods=["POST"])
def get_fees():

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
            f.total_fee,
            f.paid_fee,
            f.pending_fee,
            f.payment_status
        FROM fees f
        JOIN student s
            ON f.student_id = s.student_id
        WHERE f.student_id = :student_id
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
            "message": "Fee record not found"
        })

    return jsonify({
        "success": True,
        "student_name": row[0],
        "total_fee": float(row[1]),
        "paid_fee": float(row[2]),
        "pending_fee": float(row[3]),
        "payment_status": row[4]
    })