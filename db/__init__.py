from db.DatabaseConnection import DatabaseConnection


def init_schemas():
    _get_postgres_version()
    _create_schemas()


def _get_postgres_version():
    db = DatabaseConnection()

    with db.get_connection().cursor() as cursor:
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print('PostgreSQL database version: ' + db_version[0])


def _create_schemas():
    print("Initializing database...")
    db = DatabaseConnection()
    connection = db.get_connection()

    with connection.cursor() as cursor:
        with open("db/sql/db_init.sql", "r") as f:
            sql = f.read()
            cursor.execute(sql)

        with open("db/sql/pre_stage.sql", "r") as f:
            sql = f.read()
            cursor.execute(sql)

    print("Database successfully initialized.")





