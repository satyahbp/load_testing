import sqlite3
from typing import List, Tuple

from scripts.constants.app_configuration import DB_URL
from scripts.logging.log_module import logger as log


class SQLiteUtil():

    @staticmethod
    def data_fetch_query_executor(query: str) -> List[Tuple]:
        connection = sqlite3.connect(DB_URL, autocommit=True)
        cursor = connection.cursor()
        data_list = list()

        try:
            cursor.execute(query)
            data_list = cursor.fetchall()
        except Exception as e:
            raise Exception(e)

        cursor.close()
        connection.close()
        return data_list
    

    @staticmethod
    def insert_into_table(
        table_name: str,
        table_parameters: str,
        values: str 
    ) -> bool:

        connection = sqlite3.connect(DB_URL, autocommit=True)
        cursor = connection.cursor()

        try:
            cursor.execute(f"""
                INSERT INTO {table_name} ({table_parameters})    
                VALUES ({values})
            """)

            if cursor.rowcount < 1:
                raise Exception("Could not insert.")

        except Exception as e:
            log.error("Error in sqlite util insert: " + str(e))
            cursor.close()
            connection.close()
            return False

        cursor.close()
        connection.close()
        return True
    

    def conditional_select(
        self,
        table_name: str,
        columns: list,
        conditions: str = None,
        limit: int | None = None
    ) -> List[Tuple]:
        
        base_selection_str = "SELECT "
        data_list = list()

        # adding columns
        for each_column in columns:
            base_selection_str = base_selection_str + each_column + ", "

        if conditions:
            base_selection_str = base_selection_str[:-2] + f" FROM {table_name} WHERE {conditions} "
        else:
            base_selection_str = base_selection_str[:-2] + f" FROM {table_name} "

        if limit:
            base_selection_str = base_selection_str + f"LIMIT {limit}"

        try:
            data_list = self.data_fetch_query_executor(base_selection_str)
        except Exception as e:
            log.error("Error while fetching conditional data from db: " + str(e))
        
        return data_list
    

    @staticmethod
    def update_rows(
        table_name: str,
        update_statement: str,
        conditions: str
    ) -> bool:
        
        connection = sqlite3.connect(DB_URL, autocommit=True)
        cursor = connection.cursor()

        try:
            cursor.execute(f"""
                UPDATE {table_name} 
                SET {update_statement}
                WHERE {conditions}
            """)
        except Exception as e:
            log.error("Error while updating the row in db: " + str(e))
            cursor.close()
            connection.close()
            return False
        
        cursor.close()
        connection.close()

        return True
    

    @staticmethod
    def conditional_delete(
        table_name: str,
        conditions: str
    ) -> bool:
        connection = sqlite3.connect(DB_URL, autocommit=True)
        cursor = connection.cursor()

        try:
            cursor.execute(f"""
                DELETE FROM {table_name}
                WHERE {conditions}
            """)
        except Exception as e:
            log.error("Error while deleting from: " + table_name)
            cursor.close()
            connection.close()
            return False
        
        cursor.close()
        connection.close()

        return True