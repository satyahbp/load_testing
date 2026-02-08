import os
import configparser

config = configparser.ConfigParser()
config.read("conf/application.conf")
 
SERVICE_SECTION = "SERVICE"
LOG_SECTION = "LOG"
DATABASE_SECTION = "DATABASE"

# service
HOST = config.get(SERVICE_SECTION, "host")
PORT = int(config.get(SERVICE_SECTION, "port"))
WORKERS = int(config.get(SERVICE_SECTION, "workers"))

# logs
LOG_NAME = config.get(LOG_SECTION, "log_name")
LOG_BASE_PATH = config.get(LOG_SECTION, "log_path")
LOG_FILE_NAME = config.get(LOG_SECTION, "file_name")
LOG_LEVEL = config.get(LOG_SECTION, "level")
LOG_MAX_FILE_SIZE = config.get(LOG_SECTION, "max_file_size")
LOG_MAX_FILE_BACKUPS = config.get(LOG_SECTION, "max_backup")
LOG_HANDLERS = config.get(LOG_SECTION, "handlers")

# database
DB_BASE_URL = config.get(DATABASE_SECTION, "base_url")
DB_URL = config.get(DATABASE_SECTION, "url")
DB_REQUEST_RECORDS_TABLE = config.get(DATABASE_SECTION, "request_records_table") 
