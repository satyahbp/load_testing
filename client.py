import requests
import time, uuid
from asyncio import run, gather
from threading import Lock, Thread
# from concurrent.futures import ThreadPoolExecutor

lock = Lock()
success_lock = Lock()
failed_lock = Lock()

seconds_to_run = 1

global_request_counter = 0
success_request_counter = 0
failed_request_counter = 0

# domain = "http://localhost:10001"
domain = "http://localhost:8001"
proxy = "/request_records_services"
insert_endpoint = "/request_records"
fetch_endpoint = "/fetch_records"


def count_request():
    global global_request_counter
    global_request_counter += 1


def count_success_request():
    global success_request_counter
    success_request_counter += 1


def count_failed_request():
    global failed_request_counter
    failed_request_counter += 1


def make_insert_request(thread_number):
    print(f"Running thread: {thread_number}\n")
    url = domain + proxy + insert_endpoint
    new_id = str(uuid.uuid4())
    request_json = {"request_uuid": new_id}

    try:
        count_request()
        response = requests.post(
            url=url,
            json=request_json
        )

        print(f"Thread {thread_number} response: {response.json()}.\n")
        count_success_request()
    except Exception as e:
        print("Error while sending request: ", str(e))
        count_failed_request()


def main_flow():

    start_time = time.time()
    current_time = time.time() - start_time
    while (current_time < seconds_to_run):
        make_insert_request(1)
        current_time = time.time() - start_time
    
    print("=" * 70)
    print(f"Summary after {seconds_to_run} seconds:")
    print(f"Total Requests Sent: {global_request_counter}")
    print(f"Total successful request: {success_request_counter}")
    print(f"Total failed request counter: {failed_request_counter}")
    print("=" * 70)


if __name__ == "__main__":
    main_flow()


