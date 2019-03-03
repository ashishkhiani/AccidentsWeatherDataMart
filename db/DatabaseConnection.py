from configparser import ConfigParser

import psycopg2


class DatabaseConnection(object):
    """
    Handles the connection to the PostGreSQL database
    """

    def __init__(self):
        """
        Connects to the PostgreSQL database server
        """
        self._connection = None

        # read connection parameters
        params = self._config()

        # create connection to the PostgreSQL server
        print('***Connecting to the PostgreSQL database***')
        self._connection = psycopg2.connect(**params)

    @staticmethod
    def _config(filename='db/database.ini', section='postgresql'):
        """
        Fetches database configurations
        :param filename: config file path
        :param section: section in config to read from
        :return: config parameters
        """
        # create a parser
        parser = ConfigParser()

        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def get_connection(self):
        return self._connection

    def __del__(self):
        if self._connection is not None:
            self._connection.close()
            print('***Database connection closed***')
