from db.DatabaseConnection import DatabaseConnection


def get_postgres_version():
    db = DatabaseConnection()

    # create a cursor
    cursor = db.get_connection().cursor()

    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print('PostgreSQL database version: ' + db_version[0])

    # close the communication with the PostgreSQL
    cursor.close()
