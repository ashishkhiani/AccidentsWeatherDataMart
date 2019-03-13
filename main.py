from app.data_pre_staging import populate_dimensions_pre_stage
from app.data_staging import populate_dimensions_data_mart, create_relations
from db import init_schemas

if __name__ == '__main__':
    init_schemas()

    populate_dimensions_pre_stage(
        hour=False,
        weather=False,
        accident=True,
        location=False
    )

    populate_dimensions_data_mart(
        hour=False,
        weather=False,
        accident=False,
        location=False
    )

    create_relations(
        weather_hour=False,
        weather_location=False,
        accident_hour=False,
        accident_location=False
    )
