import os

from flask import Flask, render_template, request, jsonify, session, redirect
from db import get_connection


# ==========================================
# FLASK CONFIGURATION
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)

app.secret_key = "college-erp-development-key"


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# ATTENDANCE PAGE
# ==========================================

@app.route("/attendance")
def attendance_page():

    return render_template("attendance.html")


# ==========================================
# ATTENDANCE API
# ==========================================

@app.route("/api/attendance", methods=["POST"])
def get_attendance():

    data = request.get_json()

    student_id = data.get("student_id")

    if not student_id:
        return jsonify({
            "success": False,
            "message": "Student ID is required"
        }), 400

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                c.course_name,
                a.attended_classes,
                a.total_classes
            FROM attendance a
            JOIN course c
                ON a.course_id = c.course_id
            WHERE a.student_id = :student_id
        """

        cursor.execute(
            query,
            student_id=student_id
        )

        rows = cursor.fetchall()

        attendance_data = []

        for row in rows:

            course_name = row[0]
            attended = row[1]
            total = row[2]

            percentage = 0

            if total > 0:
                percentage = round(
                    (attended / total) * 100,
                    2
                )

            attendance_data.append({
                "course": course_name,
                "attended": attended,
                "total": total,
                "percentage": percentage
            })

        return jsonify({
            "success": True,
            "data": attendance_data
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ==========================================
# FEES PAGE
# ==========================================

@app.route("/fees")
def fees_page():

    return render_template("fees.html")


# ==========================================
# FEES API
# ==========================================

@app.route("/api/fees", methods=["POST"])
def get_fees():

    data = request.get_json()

    student_id = data.get("student_id")

    if not student_id:

        return jsonify({
            "success": False,
            "message": "Student ID is required"
        }), 400

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                total_fee,
                paid_fee,
                pending_fee,
                payment_status
            FROM fees
            WHERE student_id = :student_id
        """

        cursor.execute(
            query,
            student_id=student_id
        )

        row = cursor.fetchone()

        if not row:

            return jsonify({
                "success": False,
                "message": "Fee record not found"
            }), 404

        return jsonify({
            "success": True,
            "data": {
                "total": row[0],
                "paid": row[1],
                "pending": row[2],
                "status": row[3]
            }
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ==========================================
# RESULTS PAGE
# ==========================================

@app.route("/results")
def results_page():

    return render_template("results.html")


# ==========================================
# RESULTS API
# ==========================================

@app.route("/api/results", methods=["POST"])
def get_results():

    data = request.get_json()

    student_id = data.get("student_id")

    if not student_id:

        return jsonify({
            "success": False,
            "message": "Student ID is required"
        }), 400

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                c.course_name,
                r.marks,
                r.grade,
                r.result_status
            FROM results r
            JOIN course c
                ON r.course_id = c.course_id
            WHERE r.student_id = :student_id
        """

        cursor.execute(
            query,
            student_id=student_id
        )

        rows = cursor.fetchall()

        results = []

        for row in rows:

            results.append({
                "course": row[0],
                "marks": row[1],
                "grade": row[2],
                "status": row[3]
            })

        return jsonify({
            "success": True,
            "data": results
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ==========================================
# LOGIN PAGE
# ==========================================

@app.route("/login")
def login_page():

    return render_template("login.html")


# ==========================================
# LOGIN API
# ==========================================

@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                username,
                role,
                student_id
            FROM users
            WHERE username = :username
            AND password = :password
        """

        cursor.execute(
            query,
            username=username,
            password=password
        )

        row = cursor.fetchone()

        if not row:

            return jsonify({
                "success": False,
                "message": "Invalid username or password"
            }), 401

        session["username"] = row[0]
        session["role"] = row[1]
        session["student_id"] = row[2]

        return jsonify({
            "success": True,
            "role": row[1]
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session["role"]
    )


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ==========================================
# NOTICES API
# ==========================================

@app.route("/api/notices", methods=["GET"])
def get_notices():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                notice_id,
                title,
                description,
                notice_date
            FROM notices
            ORDER BY notice_date DESC
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        notices = []

        for row in rows:

            notices.append({
                "notice_id": row[0],
                "title": row[1],
                "description": row[2],
                "notice_date": str(row[3])
            })

        return jsonify(notices)

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    print("==========================================")
    print("COLLEGE ERP")
    print("==========================================")

    print("App location:")
    print(BASE_DIR)

    print("Templates location:")
    print(TEMPLATES_DIR)

    print("Attendance template:")
    print(
        os.path.join(
            TEMPLATES_DIR,
            "attendance.html"
        )
    )

    print(
        "Attendance template exists:",
        os.path.exists(
            os.path.join(
                TEMPLATES_DIR,
                "attendance.html"
            )
        )
    )

    print("==========================================")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )