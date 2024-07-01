from mysql.connector import Error
from .db_config import get_connection

# Create a connection to the database
connection = get_connection()

# Execute sql queries
def execute_query(connection, query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")

# Define a function  to create the database and table
def create_database_and_table():
    connection = get_connection()

    try:
        database_name = 'directify_db'
        table_name = 'user_data'

        create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        execute_query(connection, create_database_query)

        use_database_query = f"USE {database_name}"
        execute_query(connection, use_database_query)

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            User_id INT PRIMARY KEY AUTO_INCREMENT,
            User_name VARCHAR(500) NOT NULL,
            User_email VARCHAR(500) NOT NULL,
            Phone_number VARCHAR(20) NOT NULL,
            Resume_score VARCHAR(8) NOT NULL,
            Timestamp VARCHAR(50) NOT NULL,
            Page_no VARCHAR(5) NOT NULL,
            Predicted_Field BLOB NOT NULL,
            User_level BLOB NOT NULL,
            Actual_skills BLOB NOT NULL,
            Recommended_skills BLOB NOT NULL,
            Recommended_courses BLOB NOT NULL
        );
        """
        execute_query(connection, create_table_query)
        print("Database and table created successfully")

    except Error as err:
        print(f"Error: '{err}'")
    finally:
        connection.close()


def insert_data(user_name, user_email, phone_number, resume_score, timestamp, page_no, recored_field, candidate_level, skills, recommended_skills, courses):
    connection = get_connection()
    cursor = connection.cursor()
    table_name = 'user_data'

    query = f"""
    INSERT INTO {table_name} (
        User_name, User_email, Phone_number, Resume_score, Timestamp, Page_no, Predicted_Field, User_level, Actual_skills, Recommended_skills, Recommended_courses
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    rec_values = (user_name, user_email, phone_number, resume_score, timestamp, page_no, recored_field, candidate_level, skills, recommended_skills, courses)
    

    try:
        
        cursor.execute(query, rec_values)
        connection.commit()
        print("Data inserted successfully")
    except Error as err:
        print(f"Error: '{err}'")
