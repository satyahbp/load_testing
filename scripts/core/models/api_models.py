from pydantic import BaseModel

class RequestRecordsModel(BaseModel):
    request_uuid: str