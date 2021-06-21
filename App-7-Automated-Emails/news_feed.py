import requests
import pprint

# API KEY=f3526a707083479b9cdd627ead38ffed
class NewsFeed:

    URL = "https://newsapi.org/v2/top-headlines?"
    API = "f3526a707083479b9cdd627ead38ffed"

    def __init__(self, country, category):
        self.category = category
        self.country = country

    def get_info(self):
        articles = self._get_articles()

        email_body = self._create_email_body(articles)

        return email_body

    def _get_articles(self):
        url = f"{self.URL}country={self.country}&category={self.category}&apiKey={self.API}"
        response = requests.get(url).json()
        articles = response['articles']
        return articles

    def _create_email_body(self, articles):
        email_body = ''
        for i in articles:
            if i['author'] is None:
                email_body += i["title"] + "\n" + i["url"] + "\n\n"
            else:
                email_body += i['author'] + "\n" + i["title"] + "\n" + i["url"] + "\n\n"
        return email_body



