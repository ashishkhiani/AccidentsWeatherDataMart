from app.data_staging import populate_dimensions
from db import init_schemas

if __name__ == '__main__':
    init_schemas()

    populate_dimensions(
        hour=False,
        weather=True,
        accident=False,
        location=False
    )
