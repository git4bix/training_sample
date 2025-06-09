"""
import concurrent.futures
import time
def process(number):
    _ = number * 1_000_000 ** 1_000_000
    print("finish computation")

if __name__=="__main__":
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        x = executor.submit(process, 3)
        y = executor.submit(input, "Enter number: ")
    end_time = time.time()
    print(end_time - start_time)

"""

import concurrent.futures
import requests
import time

def fetch_url(url):
    return requests.get(url).status_code

urls = [ 'https://httpbin.org/delay/5',
'https://httpbin.org/delay/7']

if __name__=="__main__":
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_url, urls)
    end_time = time.time()

print(end_time - start_time)