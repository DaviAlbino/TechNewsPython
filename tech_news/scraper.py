import requests
import time
from parsel import Selector


# Requisito 1 - iniciando o projeto
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3,
        )
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    all_entry_news = selector.css('h2.entry-title a::attr(href)').getall()
    return all_entry_news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    url_news = 'https://blog.betrybe.com/'
    html = fetch(url_news)
    links_new = scrape_updates(html)
    print(links_new)
