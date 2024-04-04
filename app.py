from flask import Flask, render_template
import requests

api_key = "57b3d49680ef46149e2f418004313e95"
app = Flask(__name__)


def fetch_data(category):
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}")
    news_data = response.json()  # they can provide news dict.
    articles = news_data["articles"]
    return articles


def fetch_current_news():
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
    news_data = response.json()  # they can provide news dict.
    articles = news_data["articles"]
    return articles


@app.route("/")
def home_page():
    current_news = fetch_current_news()
    news_category = ["business", "entertainment", "health", "science", "sports", "technology"]
    business_news = fetch_data(news_category[0])
    entertainment_news = fetch_data(news_category[1])
    health_news = fetch_data(news_category[2])
    science_news = fetch_data(news_category[3])
    sports_news = fetch_data(news_category[4])
    technology_news = fetch_data(news_category[5])

    return render_template("index.html",
                           current_news=current_news,
                           business_news=business_news,
                           entertainment_news=entertainment_news,
                           health_news=health_news,
                           science_news=science_news,
                           sports_news=sports_news,
                           technology_news=technology_news,
                           )


if __name__ == "__main__":
    app.run(debug=True)
