from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock

mock_news = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
        "title": "noticia_0",
        "timestamp": "23/11/2020",
        "writer": "Escritor_0",
        "reading_time": 2,
        "summary": "Sumario da noticia_0",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "writer": "Eu",
        "summary": "Algo muito bacana aconteceu",
        "reading_time": 4,
        "timestamp": "04/04/2021",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia bacana 2",
        "writer": "Você",
        "summary": "Algo muito bacana aconteceu de novo",
        "reading_time": 16,
        "timestamp": "07/04/2022",
        "category": "Novidades",
    },
]


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_news)
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-2)
    my_time = ReadingPlanService.group_news_for_available_time(10)
    assert len(my_time["unreadable"]) == 1
    assert my_time["readable"][0]["unfilled_time"] == 4
    assert my_time["readable"][0]["chosen_news"] == [
        ('noticia_0', 2), ('Notícia bacana', 4)
    ]
