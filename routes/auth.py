from flask import Blueprint, request, jsonify, session, render_template
from db import get_connection

auth_bp = Blueprint("auth", __name__)


# Login page
@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")


# Login API
@auth_bp.route("/api/login", methods=["POST"])
def login_user():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Username and password are required"
        })

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT username, role, student_id
        FROM users
        WHERE username = :username
        AND password = :password
    """

    cursor.execute(
        query,
        username=username,
        password=password
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:

        session["username"] = user[0]
        session["role"] = user[1]
        session["student_id"] = user[2]

        return jsonify({
            "success": True,
            "message": "Login successful",
            "role": user[1]
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    })


# Logout
@auth_bp.route("/logout")
def logout():

    session.clear()

    return jsonify({
        "success": True,
        "message": "Logged out successfully"
    })