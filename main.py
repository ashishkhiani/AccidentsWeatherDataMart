from db.queries import get_postgres_version, init_db

if __name__ == '__main__':
    get_postgres_version()
    init_db()
