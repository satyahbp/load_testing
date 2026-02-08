from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from scripts.logging.log_module import logger as log
from scripts.constants.app_constants import (
    Endpoints, Tags,
    ResponseMessages, StatusCodes
)
from scripts.core.models.api_models import RequestRecordsModel
from scripts.core.handlers.request_records_handler import RequestRecordsHandler

RecordServices = APIRouter(
    prefix=Endpoints.PREFIX__REQUEST_RECORDS,
    tags=[Tags.REQUEST_RECORDS_SERVICES_TAG]
)

request_record_obj = RequestRecordsHandler()

@RecordServices.post(path=Endpoints.REQUEST_RECORDS)
async def request_recors_function(input_json: RequestRecordsModel, request: Request):
    response_json = ResponseMessages.STATUS_FAILED
    try:
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(",")[0].strip()
        else:
            client_ip = request.client.host

        log.debug("Requst From IP: " + client_ip)
        log.debug("Received Input: " + input_json.request_uuid)

        response_json = await request_record_obj.request_handler_main(
            input_json=input_json,
            client_ip=client_ip
        )

        return_json = JSONResponse(
            content = response_json,
            status_code = StatusCodes.SUCCESS_CREATE_NEW_RESOURCE
        )
    except Exception as e:
        log.error(str(e))
        return_json = JSONResponse(
            content = response_json,
            status_code = StatusCodes.INTERNAL_SERVER_ERROR
        )

    return return_json


@RecordServices.get(path=Endpoints.FETCH_RECORDS)
async def fetch_records_function(request: Request, no_of_records: int | None = None):
    response_json = ResponseMessages.STATUS_FAILED
    try:
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(",")[0].strip()
        else:
            client_ip = request.client.host

        log.debug("Requst From IP: " + client_ip)
        if no_of_records:
            log.debug("Number of records to fetch: " + str(no_of_records))
        else: 
            log.debug("Number of records to fetch: ALL!")

        response_json = await request_record_obj.fetch_db_rows_with_limits(no_of_records=no_of_records)

        return_json = JSONResponse(
            content = response_json,
            status_code = StatusCodes.SUCCESS
        )
    except Exception as e:
        log.error(str(e))
        return_json = JSONResponse(
            content = response_json,
            status_code = StatusCodes.INTERNAL_SERVER_ERROR
        )

    return return_json


