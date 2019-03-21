from db import init_schemas, DataSource

if __name__ == '__main__':
    init_schemas()

    data_source = DataSource(
        # populate_calgary_collision_data=True,
        populate_ottawa_collision_data=False,
        populate_toronto_collision_data=False,
        populate_ontario_climate_data=False,
        populate_alberta_climate_data=False,
        # populate_calgary_climate_data=True,
        populate_ottawa_climate_data=True,
        populate_toronto_climate_data=True,
        populate_raw_station_inventory_data=True,
        populate_station_inventory_data=True,
    )

    data_source.populate()
