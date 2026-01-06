import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title")
    return title.text if title else None


def run():
    url = "https://example.com"
    fetch_title(url)


if __name__ == "__main__":
    run()
