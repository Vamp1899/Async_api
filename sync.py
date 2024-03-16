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
        return dicti.json()

@timer()
def main():
    ans = []
    with requests.Session() as session:
        for _ in range(FETCHING_ITER):
            ans.append(fetch(session, URL))
    print(ans[:PRINT_ITER])
