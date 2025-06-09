import concurrent.futures
import requests
import time


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} status {requests.get.status_code}")
    except:
        print(f"{url} failed to reach.")

def read_websites(file_path):
    with open(file_path, 'r') as file:
        websites = file.readlines()
        return [website.strip() for website in websites]

if __name__ =='__main__':
    start_time = time.time()

    # Read websites from 'websites.txt'
    websites = read_websites('websites.txt')

    # Check every website sequentially
    #for website in websites:
        #check_website(website)
    if __name__ == "__main__":
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(check_website, websites)

    # Stop the timer and calculate elapsed time
    end_time = time.time()
    print(end_time - start_time)