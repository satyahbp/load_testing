# Endpoints
class Endpoints:
    # request records
    PREFIX__REQUEST_RECORDS = "/request_records_services"
    REQUEST_RECORDS = "/request_records"
    FETCH_RECORDS = "/fetch_records"


class Tags:
    REQUEST_RECORDS_SERVICES_TAG = "Request Records Services"


class StringConstants:
    STATUS = "status"
    MESSAGE = "message"
    SUCCESS = "success"
    FAILED = "failed"
    DATA = "data"


class ResponseMessages:
    STATUS_FAILED = {
        "status": "failed",
        "message": "Error occurred while processing the request."
    }


class StatusCodes:
    SUCCESS = 200
    SUCCESS_CREATE_NEW_RESOURCE = 201
    SUCCESS_NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNPROCESSABLE_CONTENT = 422
    INTERNAL_SERVER_ERROR = 500