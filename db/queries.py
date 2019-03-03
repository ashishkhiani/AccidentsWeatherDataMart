from db.DatabaseConnection import DatabaseConnection


def init_db():
    print("Initializing database...")
    db = DatabaseConnection()
    connection = db.get_connection()

    with connection.cursor() as cursor:
        sql = open("db/sql/db_init.sql", "r").read()
        cursor.execute(sql)

    print("Database successfully initialized.")


def get_postgres_version():
    db = DatabaseConnection()

    with db.get_connection().cursor() as cursor:
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print('PostgreSQL database version: ' + db_version[0])
