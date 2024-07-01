# Import mysql-connector-python for interacting with MySQL databases
import mysql.connector
from mysql.connector import Error

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '2539'
DB_NAME = 'directify_db'

def get_connection():
    connection = None

    try:
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            passwd = DB_PASSWORD,
            database = DB_NAME

        )
        print("MySQL Database connection successful")
        return connection

    except Error as err:
        print(f"Error: '{err}")
        return None