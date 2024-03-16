import asyncio
import aiohttp
import time

from constant import URL, FETCHING_ITER, PRINT_ITER

# Define the timer decorator outside the module to avoid circular import
def timer(funci):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = funci(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time {end_time - start_time}")
        return result
    return wrapper

async def fetch(session, URL):
    async with session.get(URL) as response:
        data = await response.json()
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        task = [fetch(session, URL) for _ in range(FETCHING_ITER)]
        results = await asyncio.gather(*task)
        print(results[:PRINT_ITER])

@timer
def func():
    asyncio.run(main())

# Call the function
func()