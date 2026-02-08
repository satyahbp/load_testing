from sqlite3 import connect

from scripts.constants.app_configuration import (
    DB_URL
)
from scripts.constants.queries import(
    generate_create_table_query
)
from scripts.logging.log_module import logger as log


def execute_create_query(query):
    db_connection = connect(DB_URL)
    cursor = db_connection.cursor()
    try:
        cursor.execute(query)
    except Exception as e:
        log.error(str(e))
        raise Exception("Error in table creation.")
    
    cursor.close()
    db_connection.close()


def create_records_table():
    try:
        log.info("Generating records table...")
        query = generate_create_table_query()
        execute_create_query(query)
    except Exception as e:
        log.error(str(e))
        exit(1)