import requests
from datetime import datetime, timedelta

def get2daysNews(category):
    url = "https://newsnow.p.rapidapi.com/newsv2"

    # Calculate the date range from 5 days ago to now
    end_date = datetime.now().strftime("%d/%m/%Y")
    start_date = (datetime.now() - timedelta(days=2)).strftime("%d/%m/%Y")

    payload = {
        "query": category,
        "page": 1,
        "time_bounded": True,
        "from_date": start_date,
        "to_date": end_date,
        "location": "",
        "category": "",
        "source": ""
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "your-rapidapi-key",
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    news_data = response.json()

    titles = []
    bodies = []
    dates = []
    urls = []

    for news_item in news_data.get("news", []):
        titles.append(news_item.get("title", ""))
        bodies.append(news_item.get("body", ""))
        dates.append(news_item.get("date", ""))
        urls.append(news_item.get("url", ""))
    print('inproccess')
    return titles, bodies, dates, urls

