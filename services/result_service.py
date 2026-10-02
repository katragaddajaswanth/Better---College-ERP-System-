from db import get_connection


def get_student_results(student_id):

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

    results = []

    for row in rows:

        results.append({
            "student_name": row[0],
            "course": row[1],
            "marks": float(row[2]),
            "grade": row[3],
            "status": row[4]
        })

    return results