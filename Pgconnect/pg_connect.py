import logging
import os

import psycopg2
from psycopg2 import OperationalError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_connection(host, port, database, user, password):
    """Create and return a connection to a PostgreSQL database."""
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
        logger.info("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        logger.error("The error '%s' occurred", e)
    return connection


def execute_query(connection, query):
    """Execute a SQL query on the given connection."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logger.info("Query executed successfully")
    except OperationalError as e:
        logger.error("The error '%s' occurred", e)
    finally:
        cursor.close()


def fetch_results(connection, query):
    """Execute a SELECT query and return the results."""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except OperationalError as e:
        logger.error("The error '%s' occurred", e)
    finally:
        cursor.close()
    return result


if __name__ == "__main__":
    # Connection parameters are read from environment variables.
    # Set them before running:
    #   export PG_HOST=localhost
    #   export PG_PORT=5432
    #   export PG_DATABASE=my_database
    #   export PG_USER=my_user
    #   export PG_PASSWORD=my_password
    HOST = os.environ.get("PG_HOST", "localhost")
    PORT = int(os.environ.get("PG_PORT", 5432))
    DATABASE = os.environ.get("PG_DATABASE", "my_database")
    USER = os.environ.get("PG_USER", "my_user")
    PASSWORD = os.environ.get("PG_PASSWORD", "")

    conn = create_connection(HOST, PORT, DATABASE, USER, PASSWORD)

    if conn is not None:
        # Example: create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        execute_query(conn, create_table_query)

        # Example: fetch the PostgreSQL server version
        rows = fetch_results(conn, "SELECT version();")
        if rows:
            logger.info("PostgreSQL version: %s", rows[0][0])

        conn.close()
