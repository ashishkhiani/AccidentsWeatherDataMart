from app.data_pre_staging import populate_dimensions_pre_stage
from app.data_staging import populate_dimensions_data_mart, create_relations, create_fact_table
from db import init_schemas

if __name__ == '__main__':
    init_schemas()

    populate_dimensions_pre_stage(
        hour=True,
        weather=True,
        accident=True,
        location=True,
        event=True
    )

    create_relations(
        weather_hour=True,
        accident_hour=True,
        accident_location=True,
        weather_location=True,
        event_hour=True,
        event_location=True
    )

    populate_dimensions_data_mart(
        hour=True,
        weather=True,
        accident=True,
        location=True,
        event=True
    )

    create_fact_table(create=True)
