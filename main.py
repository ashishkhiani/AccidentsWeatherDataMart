from app.data_pre_staging import populate_dimensions_pre_stage
from app.data_staging import populate_dimensions_data_mart, create_relations, create_fact_table
from db import init_schemas

if __name__ == '__main__':
    init_schemas()

    populate_dimensions_pre_stage(
        hour=False,
        weather=False,
        accident=False,
        location=False
    )

    create_relations(
        weather_hour=False,
        accident_hour=False,
        accident_location=False,
        weather_location=False
    )

    populate_dimensions_data_mart(
        hour=False,
        weather=False,
        accident=False,
        location=False
    )

    create_fact_table(create=False)
