import uvicorn

from scripts.constants.app_configuration import HOST, PORT, WORKERS

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=HOST, 
        port=PORT, 
        workers=WORKERS
    )