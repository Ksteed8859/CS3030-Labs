import requests

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'http://ww.brokenurl.com'
]


for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} : SITE UP") 
        else:
            print(f"{url} : SITE DOWN")
    except requests.exceptions.RequestException:
        print(f"{url} : SITE DOWN")