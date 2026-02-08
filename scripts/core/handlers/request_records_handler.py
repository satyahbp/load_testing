from fastapi import Request

from scripts.constants.app_configuration import DB_REQUEST_RECORDS_TABLE
from scripts.core.models.api_models import RequestRecordsModel
from scripts.logging.log_module import logger as log
from scripts.utils.sqlite_utils import SQLiteUtil
from scripts.constants.app_constants import (
    StatusCodes,
    StringConstants,
    ResponseMessages
)

class RequestRecordsHandler:
    
    def __init__(self):
        self.sqlite_util_obj = SQLiteUtil()

    async def request_handler_main(
        self,
        input_json: RequestRecordsModel, 
        client_ip: str
    ):
        return_json = {
            StringConstants.STATUS: StringConstants.FAILED
        }
        try:
            request_records_db_parameters = "request_uuid, ip_address"
            request_records_db_values = f"""'{input_json.request_uuid}', '{client_ip}'"""
            insert_response = self.sqlite_util_obj.insert_into_table(
                table_name=DB_REQUEST_RECORDS_TABLE,
                table_parameters=request_records_db_parameters,
                values=request_records_db_values
            )
            if not insert_response:
                raise Exception("Error in inserting new URL in DB.")
            
            return_json = {
                StringConstants.STATUS: StringConstants.SUCCESS,
                StringConstants.MESSAGE: f"Created record for {input_json.request_uuid}.",
            }
        except Exception as e:
            log.error("Error while inserting the data: " + str(e))
            return_json[StringConstants.MESSAGE] = "Error in adding data."
        
        return return_json
    

    async def fetch_db_rows_with_limits(self, no_of_records: int):
        return_json = {
            StringConstants.STATUS: StringConstants.FAILED,
            StringConstants.DATA: []
        }
        try:
            db_columns = ["request_uuid", "ip_address", "received_at"]
            if no_of_records:
                db_response = self.sqlite_util_obj.conditional_select(
                    table_name=DB_REQUEST_RECORDS_TABLE,
                    columns=db_columns,
                    limit=no_of_records
                )
            else:
                db_response = self.sqlite_util_obj.conditional_select(
                    table_name=DB_REQUEST_RECORDS_TABLE,
                    columns=db_columns
                )

            if not db_response:
                raise Exception("DB query did not return anything.")
            
            data_list = list()
            for each_row in db_response:
                data_list.append({
                    "request_uuid": each_row[0],
                    "ip_address": each_row[1],
                    "received_at": each_row[2]
                })
            
            return_json[StringConstants.DATA] = data_list
            return_json[StringConstants.STATUS] = StringConstants.SUCCESS
            return_json[StringConstants.MESSAGE] = "Successfully fetched data!"
        except Exception as e:
            log.error("Error while fetching the data: " + str(e))
            return_json[StringConstants.MESSAGE] = "Error in fetching data."
        
        return return_json