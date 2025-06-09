import requests

def fetch_url(url):
    return requests.get(url).status_code

urls = 'https://httpbin.org/delay/5'


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up! and {response.status_code}")
        else:
            print(f"{url} status {response.status_code}")
    except:
        print(f"{url} failed to reach.")

print(check_website("https://httpbin.org/delay/5"))