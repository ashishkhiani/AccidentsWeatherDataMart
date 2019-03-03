Prequisites:

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
    [postgresql]
    host=web0.eecs.uottawa.ca
    port=15432
    database=group_27
    user=<uottawa_user_name>
    password=<uottawa_password>
    ```

7. Run Application

    ```
    python3 main.py
    ```



