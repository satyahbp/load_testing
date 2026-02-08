from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from scripts.core.services.request_records_services import RecordServices
from scripts.logging.log_module import logger as log
from scripts.constants.db_initialization import (
    create_records_table
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Starting the DB...")
    create_records_table()
    yield
    log.info("Ending the program...")


app = FastAPI(
    title="Load Testing Service",
    lifespan=lifespan
)


@app.middleware("http")
async def request_validator(request: Request, call_next):
    print("Request at Middleware.")

    response = await call_next(request)
    return response

app.include_router(RecordServices)


app.add_middleware(
    CORSMiddleware,
    allow_origins = "*",
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)