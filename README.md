# CONFIGURATION

Pre-requisites:

This project uses Python 3. You need to have Python 3 installed on your machine.
In addition, you will need to have pip install on your machine. 


1. Navigate to project directory

    ```
    cd AccidentsWeatherDataMart/
    ```

2. Configure PYTHONPATH. Set the PYTHONPATH to point to this project's directory.

    ```
    export PYTHONPATH="$PWD"
    ```

3. Create virtual environment

    ```
    python3 -m venv venv
    ```

4. Activate virtual environment

    ```
    source venv/bin/activate
    ```

5. Install requirements to the virtual environment

    ```
    pip install -r requirements.txt
    ```

6. Create `database.ini` file inside the `db` directory with the following format

    ```
    [localhost]
    host=localhost
    port=5432
    database=postgres
    
    [data_source_files]
    raw_station_inventory_file=db/resources/climate_data/station_inventory.csv
    collision_data_ottawa_2014=db/resources/collision_data/ottawa/allcollisions2014.csv
    collision_data_ottawa_2015=db/resources/collision_data/ottawa/allcollisions2015.csv
    collision_data_ottawa_2016=db/resources/collision_data/ottawa/allcollisions2016.csv
    collision_data_ottawa_2017=db/resources/collision_data/ottawa/allcollisions2017.csv
    collision_data_toronto=db/resources/collision_data/toronto/Fatal_Collisions.csv
    climate_data_alberta_1=db/resources/climate_data/alberta_1_1.csv
    climate_data_alberta_2=db/resources/climate_data/alberta_1_2.csv
    climate_data_alberta_3=db/resources/climate_data/alberta_2_1.csv
    climate_data_alberta_4=db/resources/climate_data/alberta_2_2.csv
    climate_data_alberta_5=db/resources/climate_data/alberta_3_1.csv
    climate_data_alberta_6=db/resources/climate_data/alberta_3_2.csv
    climate_data_ontario_1=db/resources/climate_data/ontario_1_1.csv
    climate_data_ontario_2=db/resources/climate_data/ontario_1_2.csv
    climate_data_ontario_3=db/resources/climate_data/ontario_2_1.csv
    climate_data_ontario_4=db/resources/climate_data/ontario_2_2.csv
    climate_data_ontario_5=db/resources/climate_data/ontario_3.csv
    climate_data_ontario_6=db/resources/climate_data/ontario_4.csv
    ```

7. Initialize data source (one-time step)

    ```
    python3 datasource.py
    ```
    
8. Run Application

    ```
    python3 main.py
    ```

# MISC

* Starting your local PostGreSQL instance

    ```
    pg_ctl -D /usr/local/var/postgres start
    ```
    
* Stopping your local PostGreSQL instance

    ```
    pg_ctl -D /usr/local/var/postgres stop
    ```
