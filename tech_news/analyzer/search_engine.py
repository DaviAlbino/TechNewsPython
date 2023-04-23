from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    found_news = []
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    for piece in news_list:
        found_news.append((piece["title"], piece["url"]))
    return found_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    found_news = []
    news_li = search_news({"category": {"$regex": category, "$options": "i"}})
    for piece in news_li:
        found_news.append((piece["title"], piece["url"]))
    return found_news
