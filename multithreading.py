import json
import timeit, time
import requests
import multiprocessing
from multiprocessing.pool import Pool
import concurrent.futures
from constant import URL, FETCHING_ITER, PRINT_ITER

def timer():
    def wrapper(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time {end_time - start_time}")
    return wrapper

def fetch(session, URL):
    with session.get(URL) as dicti:
        if dicti.status_code == 200:
            return dicti.json()
        return f"Error in getting response {dicti.status_code}"

@timer()
def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        with requests.Session() as session:
            futures = [executor.submit(fetch, session, URL) for _ in range(FETCHING_ITER)]
            ans = [future.result() for future in concurrent.futures.as_completed(futures[:PRINT_ITER])]
            try:
                 print(ans)
            except Exception as e:
                print("Error occured ", e)