import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    next_link = selector.css('a.next::attr(href)').get()
    if (next_link):
        return next_link
    else:
        None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    reading = selector.css('li.meta-reading-time::text').get().split(" ")[0]
    smr = selector.css('div.entry-content p').xpath('string()').get().strip()
    news_dict = {
        'url': selector.css("link[rel='canonical']::attr(href)").get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('span.author > a.url::text').get(),
        'reading_time': int(reading),
        'summary': smr,
        "category": selector.css('span.label::text').get(),
    }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    news_create = []
    trybe_url = 'https://blog.betrybe.com/'
    links_list = []

    while amount > len(links_list):
        current_page = fetch(trybe_url)
        links_list.extend(scrape_updates(current_page))
        trybe_url = scrape_next_page_link(current_page)

    links_list_news = links_list[:amount]
    for link in links_list_news:
        scraped_link = scrape_news(fetch(link))
        news_create.append(scraped_link)
    create_news(news_create)
    return news_create


if __name__ == '__main__':
    url_news = 'https://blog.betrybe.com/'
    html = fetch(url_news)
    links_new = scrape_updates(html)
    next_page = scrape_next_page_link(html)
    print(next_page)
