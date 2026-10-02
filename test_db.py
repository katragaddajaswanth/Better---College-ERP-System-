from db import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
    SELECT
        USER,
        SYS_CONTEXT('USERENV', 'SERVICE_NAME'),
        SYS_CONTEXT('USERENV', 'CON_NAME')
    FROM dual
""")

print("Connection details:")
print(cursor.fetchone())

cursor.execute("""
    SELECT owner, object_name, object_type
    FROM all_objects
    WHERE object_name = 'NOTICES'
""")

print("NOTICES table:")
print(cursor.fetchall())

cursor.execute("SELECT COUNT(*) FROM notices")

print("Number of notices:")
print(cursor.fetchone()[0])

cursor.close()
connection.close()