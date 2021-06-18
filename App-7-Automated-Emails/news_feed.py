import requests
import pprint

# API KEY=f3526a707083479b9cdd627ead38ffed
class NewsFeed:

    URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f3526a707083479b9cdd627ead38ffed"

    # def __init__(self, data):
    #     self.data = data

    def get_info(self):
        response = requests.get(self.URL).json()
        articles = response['articles']

        for i in articles:
            if i['author'] == None:
                print(i['title'])
                print(i['url'])
                print()
            else:
                print(i['author'])
                print(i['title'])
                print(i['url'])
                print()




test = NewsFeed().get_info()