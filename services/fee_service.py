from db import get_connection


def get_student_fees(student_id):

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
        return None

    return {
        "student_name": row[0],
        "total_fee": float(row[1]),
        "paid_fee": float(row[2]),
        "pending_fee": float(row[3]),
        "payment_status": row[4]
    }