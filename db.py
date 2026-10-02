import oracledb


# ==========================================
# ORACLE DATABASE CONFIGURATION
# ==========================================

DB_USER = "SYSTEM"
DB_PASSWORD = "aditya"
DB_DSN = "localhost:1521/FREEPDB1"


def get_connection():

    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )

    return connection