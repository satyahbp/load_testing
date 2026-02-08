from scripts.constants.app_configuration import (
    DB_REQUEST_RECORDS_TABLE
)

def generate_create_table_query():
    query = f"""
        CREATE TABLE IF NOT EXISTS {DB_REQUEST_RECORDS_TABLE} (
            id INTEGER PRIMARY KEY,
            request_uuid TEXT,
            ip_address TEXT,
            received_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """

    return query