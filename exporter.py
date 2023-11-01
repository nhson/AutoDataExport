import logging
import os
import psycopg2 

logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s", level=logging.INFO
)

DB_CONFIG = {
    "host": os.environ.get("DB_HOSTNAME"),
    "database": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USERNAME"),
    "password": os.environ.get("DB_PASSWORD")
}

class DataExporter:
    def __init__(self):
        self.db_config = DB_CONFIG
    
    def __connect_to_database(self) -> None:
        try: 
            self.conn = psycopg2.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            logging.info("Connected to the database")
        except Exception as e:
            logging.error(
                "Failed to connect to the database with error: %s",e)
            raise
        
    def __fetch_from_db(self, start_timestamp, end_timestamp):
        self.__connect_to_database()
        query = f"""sumary_line"""
        "
